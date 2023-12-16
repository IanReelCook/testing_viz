import plotly.graph_objects as go

import pandas as pd

# Reading data from the survey CSV
df = pd.read_csv('https://github.com/marestaing/hosting/blob/main/visited_states.csv?raw=true')

fig = go.Figure(data=go.Choropleth(
    locations=df['code'],  # Spatial coordinates
    z=df['number students'].astype(float),  # Data to be color-coded
    locationmode='USA-states',  # Set of locations match entries in `locations`
    colorscale='Blues',
    colorbar_title="Number of Students",
))

fig.update_layout(
    title_text='States Visited by APCSP Students (Periods 4, 5, and 6)',
    geo_scope='usa',  # Limit map scope to USA
)

fig.show()
