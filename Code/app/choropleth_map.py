import dash
from dash import dcc, html
import geopandas as gpd
import pandas as pd
import plotly.express as px
import pycountry
import numpy as np
import json

# -------------------------
# 1. Load and preprocess COVID-19 data
# -------------------------
file_path = 'daily-new-confirmed-covid-19-cases-per-million-people.csv'
data = pd.read_csv(file_path)

# Convert the 'Day' column to datetime format
data['Day'] = pd.to_datetime(data['Day'])

# Use the entire time span available in the dataset
start_date = data['Day'].min()  # Earliest date in the data
end_date = data['Day'].max()    # Latest date in the data

# Filter the data to the selected time period
filtered_data = data[(data['Day'] >= start_date) & (data['Day'] <= end_date)]

# Remove non-country entities
non_countries = [
    "Africa", "Asia", "Asia excl. China", "European Union",
    "Europe", "High income", "Low income", "Lower middle income",
    "North America", "Oceania", "South America", "Upper middle income",
    "World", "European Union (27)", "High-income countries",
    "Low-income countries", "Lower-middle-income countries",
    "Upper-middle-income countries", "World excl. China",
    "World excl. China and South Korea",
    "World excl. China, South Korea, Japan and Singapore"
]
filtered_data = filtered_data[~filtered_data['Entity'].isin(non_countries)]

# Manual corrections for country names to ISO_A3 codes
country_name_corrections = {
    "United States": "USA",
    "China": "CHN",
    "Russia": "RUS",
    "South Korea": "KOR",
    "Iran": "IRN",
    "Vietnam": "VNM",
    "Venezuela": "VEN",
    "Syria": "SYR",
    "Laos": "LAO",
    "Bolivia": "BOL",
    "Brunei": "BRN",
    "Congo": "COD",  # Democratic Republic of the Congo
    "Czechia": "CZE",  # Czech Republic
    "Taiwan": "TWN",
    "Tanzania": "TZA",
    "Vatican": "VAT",
    "Cote d'Ivoire": "CIV",
    "Cape Verde": "CPV",
    "Democratic Republic of Congo": "COD",
    "East Timor": "TLS",
    "Kosovo": "XKX",
    "Micronesia (country)": "FSM",
    "North Korea": "PRK",
    "Palestine": "PSE",
    "Reunion": "REU",
    "United States Virgin Islands": "VIR",
    "Bonaire Sint Eustatius and Saba": "BES",
    "Curacao": "CUW",
    "Falkland Islands": "FLK",
    "Saint Barthelemy": "BLM",
    "Saint Helena": "SHN"
}

def convert_to_iso3(country_name):
    if country_name in country_name_corrections:
        return country_name_corrections[country_name]
    try:
        country = pycountry.countries.lookup(country_name)
        return country.alpha_3
    except LookupError:
        return None

# Add a new column with ISO_A3 country codes and drop rows with conversion failures
filtered_data['country_code_iso3'] = filtered_data['Entity'].apply(convert_to_iso3)
filtered_data = filtered_data.dropna(subset=['country_code_iso3'])

# -------------------------
# 2. Load world shapefile and merge with COVID-19 data
# -------------------------
shapefile_path = 'ne_110m_admin_0_countries.shp'
world = gpd.read_file(shapefile_path)

# Merge the COVID data (for all dates) with the world shapefile using ISO_A3 codes
world_merged = world.merge(filtered_data, how='left', left_on='ISO_A3', right_on='country_code_iso3')

# -------------------------
# 3. Sampling: Reduce the number of animation frames (sample one frame per week)
# -------------------------
sample_dates = pd.date_range(start_date, end_date, freq='7D')
world_merged = world_merged[world_merged['Day'].isin(sample_dates)]

# Create a string version of the date column for animation frames
world_merged['Day_str'] = world_merged['Day'].dt.strftime("%Y-%m-%d")

# -------------------------
# 4. Pre-transform the daily cases for better color scaling
# -------------------------
# Note: Make sure the column name matches exactly the CSV file's column,
# for example: 'Daily new confirmed cases of COVID-19 per million people (rolling 7-day average, right-aligned)'
world_merged['log_daily_cases'] = np.log1p(
    world_merged['Daily new confirmed cases of COVID-19 per million people (rolling 7-day average, right-aligned)']
)

# Calculate the global color scale range to keep the colorbar consistent during animation
global_min = world_merged['log_daily_cases'].min()
global_max = world_merged['log_daily_cases'].max()

# Convert the world shapefile to GeoJSON format for better plotting performance
world_geojson = json.loads(world.to_json())

# -------------------------
# 5. Create an animated choropleth map
# -------------------------
fig = px.choropleth(
    world_merged,
    geojson=world_geojson,
    locations="ISO_A3",  # Use ISO_A3 as the country identifier
    featureidkey="properties.ISO_A3",
    color='log_daily_cases',
    range_color=[global_min, global_max],  # Fix the color scale range
    hover_name='NAME',
    animation_frame='Day_str',
    color_continuous_scale='Oranges',
    projection="natural earth",
    title="COVID-19 Daily New Confirmed Cases per Million People (7-day Rolling Average) Over Time",
    labels={'log_daily_cases': 'Log-transformed Daily New Cases'}
)

# Update the map layout: auto-fit map bounds and hide geographic axes
fig.update_geos(fitbounds="locations", visible=False)

# -------------------------
# 6. Build the Dash app
# -------------------------
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("COVID-19 Animated Choropleth Map"),
    dcc.Graph(id="choropleth-map", figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)