import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# Assuming spacex_df is your DataFrame and it has a column named 'Launch Site'
# Load your actual DataFrame here
spacex_df = pd.read_csv("file:///home/project/spacex_launch_dash.csv")

# Generate options list from the DataFrame
launch_sites = spacex_df['Launch Site'].unique()
options = [{'label': 'All Sites', 'value': 'ALL'}] + [{'label': site, 'value': site} for site in launch_sites]

# Dropdown component
dropdown = dcc.Dropdown(
    id='site-dropdown',
    options=options,
    value='ALL',
    placeholder="Select a Launch Site here",
    searchable=True
)

# Create Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard", style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    dropdown
])

if __name__ == '__main__':
    app.run_server(debug=True)
