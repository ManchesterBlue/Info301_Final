import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import numpy as np

# Load dataset and clean column names
data = pd.read_csv('1.csv', low_memory=False)
data.columns = data.columns.str.strip()

# Convert 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'], errors='coerce')

# Filter data within a reasonable date range
data = data[(data['date'] >= '2019-01-01') & (data['date'] <= '2025-01-01')]

# Convert relevant columns to numeric format
cols = ['confirmed', 'government_response_index', 'stringency_index', 'hosp', 'latitude', 'longitude']
for col in cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Drop rows with missing geographic information
data = data.dropna(subset=['iso_alpha_3', 'latitude', 'longitude'])

# Forward-fill missing values to ensure each country has continuous data over time
data.sort_values(['iso_alpha_3', 'date'], inplace=True)
data[['stringency_index', 'government_response_index', 'confirmed']] = data.groupby('iso_alpha_3')[
    ['stringency_index', 'government_response_index', 'confirmed']
].ffill()

# Create a choropleth map with a time slider
fig = px.choropleth(
    data,
    locations="iso_alpha_3",  # Country ISO code
    color="stringency_index",  # Color represents the stringency index
    hover_name="administrative_area_level_1",  # Hover text displays the administrative area name
    hover_data={
        'stringency_index': True,
        'government_response_index': True,
        'confirmed': True
    },
    color_continuous_scale="Viridis",
    range_color=[0, 100],  # Ensure consistent color range across all frames
    animation_frame="date",  # Enable time slider for animation
    projection="natural earth",
    title="Geospatial Visualization: Policy Response and COVID-19 Health Data Over Time"
)

# Create a scatter plot to visualize confirmed cases over time
scatter = px.scatter_geo(
    data,
    lat='latitude',  # Latitude coordinate
    lon='longitude',  # Longitude coordinate
    size=np.sqrt(data['confirmed'].fillna(0)),  # Scale confirmed cases using square root
    hover_name="administrative_area_level_1",
    hover_data={
        'confirmed': True,
        'government_response_index': True,
        'stringency_index': True
    },
    animation_frame="date",  # Ensure scatter plot updates over time
    projection="natural earth"
)

# Overlay scatter plot onto choropleth map
for trace in scatter.data:
    fig.add_trace(trace)

# Update map layout to enhance visual clarity
fig.update_layout(
    geo=dict(
        showland=True,
        landcolor="rgb(217, 217, 217)",
        showcountries=True,
        countrycolor="Black"
    )
)

# Build the Dash app
app = dash.Dash(__name__)

# Define the app layout with a title and the interactive map
app.layout = html.Div([
    html.H1("Geospatial Visualization: Policy Response and COVID-19 Health Data Over Time"),
    dcc.Graph(id="choropleth-map", figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)