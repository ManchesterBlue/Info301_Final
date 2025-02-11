import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Load dataset and clean column names
data = pd.read_csv('1.csv', low_memory=False)
data.columns = data.columns.str.strip()

# Convert 'date' to datetime format
data['date'] = pd.to_datetime(data['date'], errors='coerce')

# Filter out invalid dates
data = data[(data['date'] >= '2019-01-01') & (data['date'] <= '2025-01-01')]

# Convert relevant columns to numeric
numeric_cols = ['confirmed', 'deaths', 'recovered', 'tests', 'people_vaccinated', 'people_fully_vaccinated']
for col in numeric_cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Ensure 'administrative_area_level_1' exists
if 'administrative_area_level_1' not in data.columns:
    raise ValueError("Column 'administrative_area_level_1' not found in the dataset.")

# Aggregate confirmed cases per day per country
grouped = data.groupby(['date', 'administrative_area_level_1'], as_index=False)[numeric_cols].sum()

# Apply forward-fill but do NOT fill beyond the last known value
grouped.sort_values(['administrative_area_level_1', 'date'], inplace=True)
grouped[numeric_cols] = grouped.groupby('administrative_area_level_1')[numeric_cols].ffill()

# Ensure confirmed cases are monotonically increasing
grouped['confirmed'] = grouped.groupby('administrative_area_level_1')['confirmed'].cummax()

# Compute total confirmed cases per country
total_cases = grouped.groupby('administrative_area_level_1')['confirmed'].max().reset_index()

# Select the top 10 countries
top_countries = total_cases.nlargest(10, 'confirmed')['administrative_area_level_1']

# Filter data to include only top countries
filtered_data = grouped[grouped['administrative_area_level_1'].isin(top_countries)]

# Ensure sorting by date
filtered_data = filtered_data.sort_values('date')

# Remove points where there is no data (avoid trailing zeros)
filtered_data = filtered_data[filtered_data['confirmed'] > 0]

# Sample data to reduce scatter points
N = 10
sampled_data = filtered_data.iloc[::N]

# Create interactive line plot
fig = px.line(
    filtered_data,
    x='date',
    y='confirmed',
    color='administrative_area_level_1',
    title='COVID-19 Trends in Top 10 Countries',
    labels={'confirmed': 'Confirmed Cases', 'date': 'Date', 'administrative_area_level_1': 'Country'},
    log_y=True,  # Default to log scale
    hover_data={'confirmed': True, 'date': True}
)

# Add scatter points to the plot
fig.add_scatter(
    x=sampled_data['date'],
    y=sampled_data['confirmed'],
    mode='markers',
    marker=dict(size=6, opacity=0.7, line=dict(width=0.8, color='black')),
    name="Sampled Daily Cases"
)

# Update layout (fix legend and rangeselector positions)
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=[
                dict(count=7, label="1W", step="day", stepmode="backward"),
                dict(count=30, label="1M", step="day", stepmode="backward"),
                dict(count=180, label="6M", step="day", stepmode="backward"),
                dict(count=365, label="1Y", step="day", stepmode="backward"),
                dict(step="all")
            ]
        ),
        rangeslider=dict(visible=True),
        type="date"
    ),
    yaxis=dict(
        title="Confirmed Cases"
    ),
    xaxis_title="Date",
    height=800,
    template="plotly_white",
    font=dict(family="Arial, sans-serif", size=14, color="black"),
    plot_bgcolor="white",
    paper_bgcolor="white",
    legend=dict(
        title="Country",
        orientation="v",
        yanchor="top",
        y=1,
        xanchor="right",
        x=1.2
    ),
    hovermode="x unified"
)

# Add interactive buttons to switch between log and linear scale
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            x=0.5,  # Positioning the buttons at the center
            y=1.2,  # Move above the graph
            buttons=[
                dict(
                    label="Log Scale",
                    method="relayout",
                    args=[{"yaxis.type": "log"}]  # Set y-axis to log scale
                ),
                dict(
                    label="Linear Scale",
                    method="relayout",
                    args=[{"yaxis.type": "linear"}]  # Set y-axis to linear scale
                )
            ]
        )
    ]
)

# Build the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("COVID-19 Trends in Top 10 Countries"),
    dcc.Graph(id="covid-trends-graph", figure=fig)
])

# Run the Dash app on a specified port (e.g., 8051)
if __name__ == '__main__':
    app.run_server(debug=True, port=8052)