# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# import numpy as np

# # Load datasets
# df_planets = pd.read_csv('Preprocessed_Planet_Data.csv')
# df_ranking = pd.read_csv('Final_Habitability_Data.csv')

# # Main app layout
# st.set_page_config(layout="wide")
# st.title('Stellar Analytics 2025 Dashboard')

# # Sidebar for global filters
# st.sidebar.header('Global Filters')
# selected_features = st.sidebar.multiselect('Select features to analyze', df_planets.columns)

# # Introduction and Context
# st.header('Mission Brief')
# st.write('This dashboard provides insights into potential habitable exoplanets based on our analysis of stellar and planetary data.')

# # Dataset Summary
# st.header('Dataset Overview')
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.metric("Total Planets", len(df_planets))
# with col2:
#     st.metric("Features Analyzed", len(df_planets.columns))
# with col3:
#     st.metric("Potentially Habitable", df_planets['P_HABITABLE'].sum())

# # Key Visualizations and Insights
# st.header('Key Visualizations and Insights')

# # Interactive Planetary Features Distribution
# st.subheader('Planetary Features Distribution')
# feature = st.selectbox('Select feature', ['P_MASS', 'P_RADIUS', 'P_TEMP_SURF'])
# fig = px.histogram(df_planets, x=feature, color='P_HABITABLE', marginal='box')
# st.plotly_chart(fig, use_container_width=True)

# # Correlation Heatmap
# st.subheader('Feature Correlations')
# corr_features = ['P_MASS', 'P_RADIUS', 'P_DISTANCE', 'P_TEMP_SURF', 'S_TEMPERATURE', 'S_MASS', 'S_RADIUS', 'S_LUMINOSITY']
# corr_matrix = df_planets[corr_features].corr()
# fig = px.imshow(corr_matrix, text_auto=True, aspect="auto")
# st.plotly_chart(fig, use_container_width=True)

# # Scatter Plot with ESI
# st.subheader('Earth Similarity Index (ESI) vs. Planetary Features')
# x_axis = st.selectbox('X-axis', ['P_RADIUS', 'P_MASS', 'P_TEMP_SURF'])
# y_axis = st.selectbox('Y-axis', ['Global ESI', 'Habitability Index'])
# fig = px.scatter(df_ranking, x=df_planets[x_axis], y=y_axis, color='Habitability_Category',
#                  hover_name='Planet Name', size='Habitability Index', size_max=20)
# st.plotly_chart(fig, use_container_width=True)

# # Custom Habitability Index Breakdown
# st.subheader('Top 10 Planets by Habitability Index')
# top_10 = df_ranking.sort_values('Habitability Index', ascending=False).head(10)
# fig = px.bar(top_10, x='Planet Name', y='Habitability Index', color='Habitability_Category',
#              hover_data=['Global ESI', 'Long-term Stability', 'Atmospheric Retention'])
# st.plotly_chart(fig, use_container_width=True)

# # Classification Results
# st.header('Classification Results')
# col1, col2 = st.columns(2)
# with col1:
#     hab_categories = df_ranking['Habitability_Category'].value_counts()
#     fig = px.pie(values=hab_categories.values, names=hab_categories.index, title='Habitability Categories')
#     st.plotly_chart(fig, use_container_width=True)
# with col2:
#     # Placeholder for Model Performance Metrics
#     st.subheader('Model Performance Metrics')
#     st.write('Accuracy: 0.95')
#     st.write('Precision: 0.92')
#     st.write('Recall: 0.89')
#     st.write('F1 Score: 0.91')

# # Interactive Table with Drill-down
# st.header('Interactive Planet Explorer')
# selected_planet = st.selectbox('Select a planet', df_planets['P_NAME'])
# planet_data = df_planets[df_planets['P_NAME'] == selected_planet].iloc[0]
# st.table(planet_data)

# # Advanced Visualization: 3D Scatter Plot
# st.header('3D Planet Visualization')
# fig = px.scatter_3d(df_planets, x='P_RADIUS', y='P_MASS', z='P_TEMP_SURF',
#                     color='P_HABITABLE', hover_name='P_NAME',
#                     labels={'P_RADIUS': 'Radius', 'P_MASS': 'Mass', 'P_TEMP_SURF': 'Surface Temperature'})
# st.plotly_chart(fig, use_container_width=True)

# # Time Series Analysis (if applicable)
# st.header('Planetary Discovery Timeline')
# df_planets['DISCOVERY_YEAR'] = pd.to_datetime(df_planets['P_DISCOVERY_YEAR'], format='%Y')
# yearly_discoveries = df_planets.groupby(df_planets['DISCOVERY_YEAR'].dt.year).size().reset_index(name='count')
# fig = px.line(yearly_discoveries, x='DISCOVERY_YEAR', y='count', title='Exoplanet Discoveries Over Time')
# st.plotly_chart(fig, use_container_width=True)

# # Geospatial Visualization (if applicable)
# st.header('Stellar Map')
# fig = px.scatter(df_planets, x='S_RA', y='S_DEC', color='P_HABITABLE',
#                  hover_name='P_NAME', title='Celestial Coordinates of Exoplanets')
# st.plotly_chart(fig, use_container_width=True)

# # Advanced Interactivity: Comparative Analysis
# st.header('Comparative Planet Analysis')
# planets_to_compare = st.multiselect('Select planets to compare', df_planets['P_NAME'], default=['Earth'])
# if planets_to_compare:
#     comparison_data = df_planets[df_planets['P_NAME'].isin(planets_to_compare)]
#     fig = px.parallel_coordinates(comparison_data, 
#                                   dimensions=['P_MASS', 'P_RADIUS', 'P_TEMP_SURF', 'P_GRAVITY'],
#                                   color='P_HABITABLE', labels={'P_HABITABLE': 'Potentially Habitable'})
#     st.plotly_chart(fig, use_container_width=True)

# # Natural Language Query (placeholder for future implementation)
# st.header('Ask Stellar Analytics')
# user_query = st.text_input('Ask a question about the exoplanet data:')
# if user_query:
#     st.write("This feature is coming soon! It will allow natural language queries about the dataset.")


import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Load datasets
df_planets = pd.read_csv('Preprocessed_Planet_Data.csv')
df_ranking = pd.read_csv('Final_Habitability_Data.csv')

# Merge datasets
df_merged = pd.merge(df_planets, df_ranking, left_on='P_NAME', right_on='Planet Name', how='inner')

# Main app layout
st.set_page_config(layout="wide")
st.title('Stellar Analytics 2025 Dashboard')

# Sidebar for global filters
st.sidebar.header('Global Filters')
habitable_filter = st.sidebar.multiselect('Filter by Habitability Category', 
                                          options=df_merged['Habitability_Category'].unique(),
                                          default=df_merged['Habitability_Category'].unique())

mass_range = st.sidebar.slider('Filter by Planet Mass (Earth masses)', 
                               float(df_merged['P_MASS'].min()), 
                               float(df_merged['P_MASS'].max()), 
                               (float(df_merged['P_MASS'].min()), float(df_merged['P_MASS'].max())))

# Apply filters
df_filtered = df_merged[
    (df_merged['Habitability_Category'].isin(habitable_filter)) &
    (df_merged['P_MASS'].between(mass_range[0], mass_range[1]))
]

# Introduction and Context
st.header('Mission Brief')
st.write('This dashboard provides insights into potential habitable exoplanets based on our analysis of stellar and planetary data.')

# Dataset Summary
st.header('Dataset Overview')
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Planets", len(df_filtered))
with col2:
    st.metric("Potentially Habitable", df_filtered['P_HABITABLE'].sum())
with col3:
    st.metric("Avg. Habitability Index", round(df_filtered['Habitability Index'].mean(), 2))

# Key Visualizations and Insights
st.header('Key Visualizations and Insights')

# Interactive Planetary Features Distribution
st.subheader('Planetary Features Distribution')
feature = st.selectbox('Select feature', ['P_MASS', 'P_RADIUS', 'P_TEMP_SURF', 'P_GRAVITY'])
fig = px.histogram(df_filtered, x=feature, color='Habitability_Category', marginal='box')
st.plotly_chart(fig, use_container_width=True)

# Scatter Plot: ESI vs Habitability Index
st.subheader('Earth Similarity Index (ESI) vs. Habitability Index')
fig = px.scatter(df_filtered, x='Global ESI', y='Habitability Index', 
                 color='Habitability_Category', hover_name='P_NAME',
                 size='P_RADIUS', size_max=20)
st.plotly_chart(fig, use_container_width=True)

# Top 10 Planets by Habitability Index
st.subheader('Top 10 Planets by Habitability Index')
top_10 = df_filtered.sort_values('Habitability Index', ascending=False).head(10)
fig = px.bar(top_10, x='P_NAME', y='Habitability Index', color='Habitability_Category',
             hover_data=['Global ESI', 'Long-term Stability', 'Atmospheric Retention'])
st.plotly_chart(fig, use_container_width=True)

# Classification Results
st.header('Classification Results')
hab_categories = df_filtered['Habitability_Category'].value_counts()
fig = px.pie(values=hab_categories.values, names=hab_categories.index, title='Habitability Categories')
st.plotly_chart(fig, use_container_width=True)

# Interactive Planet Explorer
st.header('Interactive Planet Explorer')
selected_planet = st.selectbox('Select a planet', df_filtered['P_NAME'])
planet_data = df_filtered[df_filtered['P_NAME'] == selected_planet].iloc[0]
col1, col2 = st.columns(2)
with col1:
    st.subheader("Planetary Characteristics")
    st.write(f"Mass: {planet_data['P_MASS']} Earth masses")
    st.write(f"Radius: {planet_data['P_RADIUS']} Earth radii")
    st.write(f"Surface Temperature: {planet_data['P_TEMP_SURF']} K")
    st.write(f"Gravity: {planet_data['P_GRAVITY']} m/s²")
with col2:
    st.subheader("Habitability Metrics")
    st.write(f"Global ESI: {planet_data['Global ESI']}")
    st.write(f"Habitability Index: {planet_data['Habitability Index']}")
    st.write(f"Long-term Stability: {planet_data['Long-term Stability']}")
    st.write(f"Atmospheric Retention: {planet_data['Atmospheric Retention']}")

# Advanced Visualization: 3D Scatter Plot
st.header('3D Planet Visualization')
fig = px.scatter_3d(df_filtered, x='P_RADIUS', y='P_MASS', z='P_TEMP_SURF',
                    color='Habitability_Category', hover_name='P_NAME',
                    labels={'P_RADIUS': 'Radius', 'P_MASS': 'Mass', 'P_TEMP_SURF': 'Surface Temperature'})
st.plotly_chart(fig, use_container_width=True)

# Comparative Analysis
# st.header('Comparative Planet Analysis')
# planets_to_compare = st.multiselect('Select planets to compare', df_filtered['P_NAME'], default=['Earth'])
# if planets_to_compare:
#     comparison_data = df_filtered[df_filtered['P_NAME'].isin(planets_to_compare)]
#     fig = px.parallel_coordinates(comparison_data, 
#                                   dimensions=['P_MASS', 'P_RADIUS', 'P_TEMP_SURF', 'P_GRAVITY', 'Global ESI', 'Habitability Index'],
#                                   color='Habitability_Category')
#     st.plotly_chart(fig, use_container_width=True)

# Correlation Analysis
st.header('Feature Correlation Analysis')
corr_features = ['P_MASS', 'P_RADIUS', 'P_TEMP_SURF', 'P_GRAVITY', 'Global ESI', 'Habitability Index']
corr_matrix = df_filtered[corr_features].corr()
fig = px.imshow(corr_matrix, text_auto=True, aspect="auto")
st.plotly_chart(fig, use_container_width=True)


# Button to go to interactive planet display
if st.button("View More About Planets"):
    st.markdown('<meta http-equiv="refresh" content="0;url=http://localhost:5173/">', unsafe_allow_html=True)