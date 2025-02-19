import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('exoplanet_dataset.csv')

# Check for missing values
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
missing_report = pd.DataFrame({'Column': df.columns, 'Missing Values': missing_values, 'Percentage': missing_percentage})
print(missing_report.sort_values(by='Percentage', ascending=False))

import numpy as np
import pandas as pd
from scipy.constants import G, sigma  # Gravitational constant & Stefan-Boltzmann constant

# Load dataset
data = pd.read_csv("/content/exoplanet_dataset.csv")

# Retain only the specified columns
columns_to_keep = [
    "P_NAME", "P_MASS", "P_RADIUS","P_DISTANCE", "P_PERIOD", "P_SEMI_MAJOR_AXIS", "P_ECCENTRICITY",
    "P_ESCAPE", "P_POTENTIAL", "P_GRAVITY", "P_FLUX", "P_TEMP_EQUIL", "P_TEMP_SURF",
    "P_HABITABLE", "P_DENSITY", "S_TEMPERATURE", "S_MASS", "S_RADIUS", "S_LUMINOSITY"
]
data = data[columns_to_keep]

# Constants
L_sun = 3.828e26  # Solar Luminosity in Watts
M_sun = 1.989e30  # Solar Mass in kg
AU_to_m = 1.496e11  # AU to meters conversion
C = 0.5
YEAR_TO_SECONDS = 3.154e7


# Fill missing values for S_MASS and S_RADIUS using mean
data['S_MASS'] = data['S_MASS'].fillna(data['S_MASS'].mean())
data['S_RADIUS'] = data['S_RADIUS'].fillna(data['S_RADIUS'].mean())
data['P_SEMI_MAJOR_AXIS']=data['P_SEMI_MAJOR_AXIS'].fillna(data['P_SEMI_MAJOR_AXIS'].mean())
data['P_DISTANCE']=data['P_DISTANCE'].fillna(data['P_DISTANCE'].mean())

# Compute Stellar Luminosity if missing
data['S_LUMINOSITY'] = data['S_LUMINOSITY'].fillna(L_sun * (data['S_MASS'] / M_sun) ** 3.5)

# Compute Stellar Temperature if missing (from Stefan-Boltzmann Law)
data['S_TEMPERATURE'] = data['S_TEMPERATURE'].fillna(
    (data['S_LUMINOSITY'] / (4 * np.pi * (data['S_RADIUS'] * 6.955e8)**2 * sigma)) ** 0.25
)

# Compute Eccentricity if missing (Using Approximate Model)
data['P_ECCENTRICITY'] = data.apply(lambda row:
    0.29 * (row['P_SEMI_MAJOR_AXIS'] / AU_to_m) ** 0.5 if pd.isnull(row['P_ECCENTRICITY']) else row['P_ECCENTRICITY'],
    axis=1
)

# P_PERIOD
data['P_PERIOD'] = data['P_PERIOD'].fillna(
    (4 * np.pi**2 * data['P_SEMI_MAJOR_AXIS']**3 / (G * data['S_MASS']))**0.5
)


# P_FLUX: Stellar Flux at Planet's Orbit
data['P_FLUX'] = data['P_FLUX'].fillna(
    data['S_LUMINOSITY'] / (4 * np.pi * (data['P_SEMI_MAJOR_AXIS'] *AU_to_m)**2)
)

# P_TEMP_EQUIL: Equilibrium Temperature
data['P_TEMP_EQUIL'] = data['P_TEMP_EQUIL'].fillna(
    data['S_TEMPERATURE'] * np.sqrt(data['S_RADIUS'] / (2 * data['P_SEMI_MAJOR_AXIS'] *AU_to_m))
)

# P_TEMP_SURF: Surface Temperature
data['P_TEMP_SURF'] = data['P_TEMP_SURF'].fillna(9.650 + 1.096 * data['P_TEMP_EQUIL'])



# P_MASS (Depends on S_MASS and S_RADIUS)
data['P_MASS'] = data['P_MASS'].fillna(data['S_MASS'] / (data['S_RADIUS'] - C))

# P_RADIUS (Depends on P_MASS and S_MASS)
data['P_RADIUS'] = data['P_RADIUS'].fillna(C + data['S_MASS'] * data['P_MASS'])


# Compute Planetary Escape Velocity if missing
data['P_ESCAPE'] = data['P_ESCAPE'].fillna((2 * G * data['P_MASS'] / data['P_RADIUS'])**0.5)

# Compute Gravitational Potential if missing
data['P_POTENTIAL'] = data['P_POTENTIAL'].fillna(-G * data['P_MASS'] / data['P_RADIUS'])

# Compute Surface Gravity if missing
data['P_GRAVITY'] = data['P_GRAVITY'].fillna(G * data['P_MASS'] / data['P_RADIUS']**2)

# Compute Density if missing
data["P_DENSITY"] = data["P_DENSITY"].fillna(data["P_MASS"] / ((4/3) * np.pi * (data["P_RADIUS"]**3)))



# Save final dataset
data.to_csv("Final_exoplanet_dataset.csv", index=False)
print("Final dataset saved as 'Final_exoplanet_dataset.csv'")

# Display remaining missing values percentage
missing_values_percentage = data.isnull().sum() / len(data) * 100
print("\nMissing values percentage after calculations:\n", missing_values_percentage)

import pandas as pd

# Load final dataset
data = pd.read_csv("Final_exoplanet_dataset.csv")

# Identify negative values in relevant columns
negative_values = data[
    (data["P_MASS"] < 0) |
    (data["P_RADIUS"] < 0) |
    (data["P_PERIOD"] < 0) |
    (data["P_DISTANCE"] < 0) |
    (data["P_SEMI_MAJOR_AXIS"] < 0) |
    (data["P_ECCENTRICITY"] < 0) |
    (data["P_ESCAPE"] < 0) |
    (data["P_POTENTIAL"] < 0) |
    (data["P_GRAVITY"] < 0) |
    (data["P_FLUX"] < 0) |
    (data["P_TEMP_EQUIL"] < 0) |
    (data["P_TEMP_SURF"] < 0) |
    (data["P_DENSITY"] < 0) |
    (data["S_TEMPERATURE"] < 0) |
    (data["S_MASS"] < 0) |
    (data["S_RADIUS"] < 0) |
    (data["S_LUMINOSITY"] < 0)
]

# Print how many rows have negative values
print(f"Total rows with negative values: {len(negative_values)}")

# Remove rows with negative values
data = data[
    (data["P_MASS"] >= 0) &
    (data["P_RADIUS"] >= 0) &
    (data["P_PERIOD"] >= 0) &
    (data["P_DISTANCE"] >= 0) &
    (data["P_SEMI_MAJOR_AXIS"] >= 0) &
    (data["P_ECCENTRICITY"] >= 0) &
    (data["P_ESCAPE"] >= 0) &
    (data["P_POTENTIAL"] >= 0) &
    (data["P_GRAVITY"] >= 0) &
    (data["P_FLUX"] >= 0) &
    (data["P_TEMP_EQUIL"] >= 0) &
    (data["P_TEMP_SURF"] >= 0) &
    (data["P_DENSITY"] >= 0) &
    (data["S_TEMPERATURE"] >= 0) &
    (data["S_MASS"] >= 0) &
    (data["S_RADIUS"] >= 0) &
    (data["S_LUMINOSITY"] >= 0)
]

# Save the final dataset
data.to_csv("Final_Preprocessed_Dataset_Final.csv", index=False)

print("\nNegative value check complete! Any invalid rows removed.")
print("Final dataset saved as 'Final_Cleaned_Exoplanet_Dataset.csv'.")
print("\nFinal Missing Values Summary:\n", data.isnull().sum())
print("\nFinal Dataset Summary Statistics:\n", data.describe())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def calculate_esi_param(x, x_ref, weight):
    if x == 0 and x_ref == 0:
        return 0
    return np.real((1 - np.abs((x - x_ref) / (x + x_ref))) ** weight)

def calculate_esi_interior(esi_radius, esi_density):
    return np.sqrt(np.clip(esi_radius * esi_density, 0, 1))

def calculate_esi_surface(esi_temperature, esi_escape_velocity):
    return np.sqrt(np.clip(esi_temperature * esi_escape_velocity, 0, 1))

def calculate_global_esi(esi_interior, esi_surface):
    return np.sqrt(np.clip(esi_interior * esi_surface, 0, 1))

# Load the dataset
data = pd.read_csv('/content/Final_Preprocessed_Dataset_Final.csv')

earth_radius = 1.0
earth_density = 1.0
earth_temperature = 288  # Kelvin
earth_escape_velocity = 1.0

weight_radius = 0.57
weight_density = 1.07
weight_temperature = 5.58
weight_escape_velocity = 0.70

# Calculate individual ESI parameters
data['esi_radius'] = data['P_RADIUS'].apply(lambda x: calculate_esi_param(x, earth_radius, weight_radius))
data['esi_density'] = data['P_DENSITY'].apply(lambda x: calculate_esi_param(x, earth_density, weight_density))
data['esi_temperature'] = data['P_TEMP_SURF'].apply(lambda x: calculate_esi_param(x, earth_temperature, weight_temperature))
data['esi_escape_velocity'] = data['P_ESCAPE'].apply(lambda x: calculate_esi_param(x, earth_escape_velocity, weight_escape_velocity))

# Calculate Interior and Surface ESIs
data['esi_interior'] = data.apply(lambda row: calculate_esi_interior(row['esi_radius'], row['esi_density']), axis=1)
data['esi_surface'] = data.apply(lambda row: calculate_esi_surface(row['esi_temperature'], row['esi_escape_velocity']), axis=1)

# Calculate Global ESI
data['esi_global'] = data.apply(lambda row: calculate_global_esi(row['esi_interior'], row['esi_surface']), axis=1)

# Save the updated dataset
#data.to_csv('output_with_esi.csv', index=False)
print("ESI calculations completed")

# Categorize planets based on Global ESI
def categorize_esi(esi):
    if esi >= 0.8:
        return 'Earth-like'
    elif esi >= 0.4:
        return 'Moderate'
    else:
        return 'Non-Habitable'

data['Category'] = data['esi_global'].apply(categorize_esi)

# Scatter plot with categories
plt.figure(figsize=(10, 8))
categories = {'Earth-like': 'green', 'Moderate': 'orange', 'Non-Habitable': 'red'}
for category, color in categories.items():
    subset = data[data['Category'] == category]
    plt.scatter(subset['esi_interior'], subset['esi_surface'], label=category, color=color, s=50, alpha=0.7)

# Add labels, legend, and title
plt.xlabel('Interior ESI', fontsize=14)
plt.ylabel('Surface ESI', fontsize=14)
plt.title('Categorized Planets: Interior vs Surface ESI', fontsize=16)
plt.legend(title='Category')
plt.grid(alpha=0.3)

# Show the plot
plt.show()

import seaborn as sns

# Histogram with Kernel Density Estimate (KDE)
plt.figure(figsize=(10, 6))
sns.histplot(data['esi_global'], kde=True, bins=30, color='blue', alpha=0.6)
plt.xlabel('Global ESI', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title('Distribution of Global ESI', fontsize=16)

# Show the plot
plt.show()

def estimate_long_term_stability(data):
    # Normalize within the function for better readability
    normalized_axis = data['P_SEMI_MAJOR_AXIS'] / data['P_SEMI_MAJOR_AXIS'].max()
    normalized_eccentricity = data['P_ECCENTRICITY'] / data['P_ECCENTRICITY'].max()
    data['long_term_stability'] = 1 - (normalized_axis * normalized_eccentricity)
    return data

def estimate_atmospheric_retention(data):
    # Normalize within the function for better readability
    normalized_escape = data['P_ESCAPE'] / data['P_ESCAPE'].max()
    normalized_temp = data['P_TEMP_SURF'] / data['P_TEMP_SURF'].max()
    data['atmospheric_retention'] = normalized_escape * (1 - normalized_temp)
    return data

# Load the dataset with pre-calculated ESI
#data = pd.read_csv('output_with_esi.csv')

# Calculate long-term stability and atmospheric retention using the revised functions
data = estimate_long_term_stability(data)
data = estimate_atmospheric_retention(data)

# Calculate Habitability Index (HI) - No changes here
data['habitability_index'] = (
    0.5 * data['esi_global'] +
    0.3 * data['long_term_stability'] +
    0.2 * data['atmospheric_retention']
)

# Normalize the Habitability Index to be between 0 and 1 - No changes here
#data['habitability_index_normalized'] = (data['habitability_index'] - data['habitability_index'].min()) / (data['habitability_index'].max() - data['habitability_index'].min())

# Save the updated dataset with all calculated features - No changes here
data.to_csv('output_with_habitability_index.csv', index=False)

print("Habitability Index calculations completed.Results saved to 'output_with_habitability_index.csv")

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/content/output_with_habitability_index.csv')

# Select features for analysis (excluding the target variable and non-numeric columns)
features = ['P_MASS', 'P_RADIUS', 'P_PERIOD', 'P_SEMI_MAJOR_AXIS', 'P_ECCENTRICITY',
            'P_ESCAPE', 'P_GRAVITY', 'P_FLUX', 'P_TEMP_EQUIL', 'P_TEMP_SURF',
            'P_DENSITY', 'S_TEMPERATURE', 'S_MASS', 'S_RADIUS', 'S_LUMINOSITY',
            'esi_radius', 'esi_density', 'esi_temperature', 'esi_escape_velocity',
            'esi_interior', 'esi_surface', 'long_term_stability',
            'atmospheric_retention']

X = df[features]
y = df['esi_global']

# ----> DIAGNOSE AND HANDLE MISSING VALUES <----

# Check for missing values in features and target
#print("Missing values in features (X):\n", X.isnull().sum())
#print("\nMissing values in target (y):", y.isnull().sum())

# OPTION 1: Remove rows with missing values
# df.dropna(subset=features + ['habitability_index'], inplace=True)

# OPTION 2: Impute missing values (e.g., with the mean)
# from sklearn.impute import SimpleImputer
# imputer = SimpleImputer(strategy='mean') # Or other strategies like 'median'
# X = imputer.fit_transform(X)
# y = imputer.fit_transform(y.values.reshape(-1, 1))  # Reshape for imputer


# ----> REST OF YOUR CODE <----


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Get feature importances
importances = rf_model.feature_importances_
feature_importance = pd.DataFrame({'feature': features, 'importance': importances})
feature_importance = feature_importance.sort_values('importance', ascending=False)

# Plot feature importances
plt.figure(figsize=(12, 8))
plt.bar(feature_importance['feature'], feature_importance['importance'])
plt.xticks(rotation=90)
plt.xlabel('Features')
plt.ylabel('Importance')
plt.title('Feature Importance for ESI Global')
plt.tight_layout()
plt.show()

# Print top 10 most important features
print("Top 10 most important features:")
print(feature_importance.head(10))


data = pd.read_csv('/content/output_with_habitability_index.csv')

# Extract the required columns including planet names
extracted_data = data[['P_NAME', 'esi_global', 'long_term_stability', 'atmospheric_retention', 'habitability_index']].copy()

# Rename columns for clarity
extracted_data = extracted_data.rename(columns={
    'P_NAME': 'Planet Name',
    'esi_global': 'Global ESI',
    'long_term_stability': 'Long-term Stability',
    'atmospheric_retention': 'Atmospheric Retention',
    'habitability_index': 'Habitability Index'
})

# Create a rank based on Habitability Index
extracted_data['Rank'] = extracted_data['Habitability Index'].rank(method='min', ascending=False)

# Sort the data by rank
extracted_data = extracted_data.sort_values('Rank')

# Save the extracted data to a new CSV file
#extracted_data.to_csv('planet_habitability_ranking.csv', index=False)

print("Data extracted, ranked, and sorted")

df = extracted_data
def classify_planet(hi, esi):
    if hi >= 0.70 and esi >= 0.85:
        return 'Potentially Habitable'
    elif hi >= 0.60 and esi >= 0.70:
        return 'Marginally Habitable'
    else:
        return 'Non-Habitable'

# Apply the classification function to create a new column
df['Habitability_Category'] = df.apply(lambda row: classify_planet(row['Habitability Index'], row['Global ESI']), axis=1)

# Save the updated DataFrame to a new CSV file
df.to_csv('planet_habitability_ranking_with_categories.csv', index=False)

print("Classification complete. Results saved to 'planet_habitability_ranking_with_categories.csv'.")

import seaborn as sns
import matplotlib.pyplot as plt

# Box plot for Habitability Index by category
plt.figure(figsize=(10, 6))
sns.boxplot(x='Habitability_Category', y='Habitability Index', data=df, palette='Set2')
plt.xlabel('Habitability Category', fontsize=14)
plt.ylabel('Habitability Index', fontsize=14)
plt.title('Distribution of Habitability Index by Category', fontsize=16)
plt.grid(alpha=0.3)
plt.show()


# Scatter plot for Global ESI vs Habitability Index
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Global ESI', y='Habitability Index', hue='Habitability_Category', data=df, palette='viridis', alpha=0.7)
plt.xlabel('Global ESI', fontsize=14)
plt.ylabel('Habitability Index', fontsize=14)
plt.title('Global ESI vs Habitability Index', fontsize=16)
plt.legend(title='Category')
plt.grid(alpha=0.3)
plt.show()

# Heatmap of correlations
correlation_matrix = df[['Global ESI', 'Long-term Stability', 'Atmospheric Retention', 'Habitability Index']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Between Features', fontsize=16)
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Habitability Index', kde=True, bins=30) # Changed data=data to data=df
plt.xlabel('Habitability Index', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title('Distribution of Habitability Index', fontsize=16)
plt.grid(alpha=0.3)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace with your file path)
data = pd.read_csv('/content/planet_habitability_ranking_with_categories.csv')

# Count the number of planets in each category
category_counts = data['Habitability_Category'].value_counts()

# Define labels and colors for the pie chart
labels = [
    f'Potentially Habitable (Green)',
    f'Marginally Habitable (Orange)',
    f'Non-Habitable (Red)'
]
colors = ['green', 'orange', 'red']  # Assign colors to categories

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Distribution of Habitability Categories', fontsize=16)
plt.show()
