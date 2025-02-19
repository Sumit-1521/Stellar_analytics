## Overview

This project focuses on analyzing exoplanet datasets to assess their habitability potential. The analysis includes data cleaning, handling missing values, calculating astrophysical parameters, and developing indices like the Earth Similarity Index (ESI) and Habitability Index (HI). The results provide insights into the potential habitability of exoplanets based on scientifically rigorous methods.

---

## Features

1. **Data Cleaning and Preprocessing**:
   - Handles missing values using astrophysical formulas.
   - Removes redundant or irrelevant columns.
   - Ensures physical consistency of planetary and stellar parameters.

2. **Key Calculations**:
   - **Earth Similarity Index (ESI)**: Measures similarity to Earth using parameters like radius, density, surface temperature, and escape velocity.
   - **Habitability Index (HI)**: Combines ESI, long-term orbital stability, and atmospheric retention to rank planets.

3. **Visualization**:
   - Scatter plots and histograms for ESI and HI distributions.
   - Heatmaps showing correlations between features.
   - Pie charts illustrating the distribution of habitability categories.

4. **Classification**:
   - Categorizes planets into three groups:
     - *Potentially Habitable*
     - *Marginally Habitable*
     - *Non-Habitable*

5. **Ranking**:
   - Ranks planets based on their Habitability Index.

---

## Dataset

The project utilizes an exoplanet dataset (`exoplanet_dataset.csv`) containing planetary and stellar parameters. After processing, the cleaned dataset is saved as `Final_Cleaned_Exoplanet_Dataset.csv`.

### Key Parameters:
- Planetary: Mass, radius, orbital period, semi-major axis, eccentricity, escape velocity, surface gravity, flux, equilibrium temperature.
- Stellar: Mass, radius, effective temperature, luminosity.

---

## Methodology

### 1. **Handling Missing Values**
Astrophysical models were used to compute missing values for critical parameters:
- Kepler's laws for orbital properties.
- Stefan-Boltzmann law for stellar temperatures.
- Newtonian mechanics for gravitational properties.

### 2. **Earth Similarity Index (ESI)**
Calculated using normalized planetary parameters:
$$
ESI = \sqrt{ESI_{Interior} \times ESI_{Surface}}
$$
Where:
- $$
 ESI_{Interior} $$: Combines radius and density.
- $$
 ESI_{Surface} $$: Combines surface temperature and escape velocity.

### 3. **Habitability Index (HI)**
Incorporates three factors:
$$
HI = 0.5 \times ESI + 0.3 \times Stability + 0.2 \times Atmospheric Retention
$$
- Stability: Derived from semi-major axis and eccentricity.
- Atmospheric Retention: Based on escape velocity and surface temperature.

### 4. **Classification**
Planets are categorized based on thresholds for HI and ESI:
- *Potentially Habitable*: $$
 HI \geq 0.70 $$ and $$
 ESI \geq 0.85 $$
- *Marginally Habitable*: $$
 HI \geq 0.60 $$ and $$
 ESI \geq 0.70 $$
- *Non-Habitable*: Below these thresholds.

---

## Results

1. **Final Datasets**:
   - `Final_Cleaned_Exoplanet_Dataset.csv`: Cleaned dataset with all missing values addressed.
   - `output_with_habitability_index.csv`: Dataset with calculated indices.
   - `planet_habitability_ranking_with_categories.csv`: Ranked planets with habitability categories.

2. **Insights**:
   - Majority of planets are non-habitable with low ESI values (0.7).
   - Key features influencing habitability include surface ESI, interior ESI, radius, density, and atmospheric retention.

3. **Visualizations**:
   - Scatter plots highlight relationships between ESI components.
   - Histograms show the distribution of HI across planets.
   - Pie charts reveal the percentage of planets in each habitability category.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone 
   cd Stellar_Analytics
   ```

2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

3. Run the main analysis script:
   ```bash
   python analyze_exoplanets.py
   ```

4. View results in the output files or generated visualizations.

---

## Key Files

- `analyze_exoplanets.py`: Main script for analysis.
- `exoplanet_dataset.csv`: Raw dataset used as input.
- `Final_Cleaned_Exoplanet_Dataset.csv`: Cleaned dataset after preprocessing.
- `output_with_habitability_index.csv`: Dataset with calculated indices.
- `planet_habitability_ranking_with_categories.csv`: Final ranked dataset with classifications.

---

## Future Work

- Incorporate additional parameters like atmospheric composition or magnetic field strength.
- Use machine learning models to predict habitability based on more complex relationships.
- Expand analysis to include multi-star systems or rogue planets.

---

## Credits

This project was developed using publicly available astrophysical datasets and formulas from sources such as NASA's Exoplanet Archive and peer-reviewed research papers (e.g., Chen & Kipping 2017).

For questions or contributions, please contact [sumitkumarsheoran89@gmail.com].

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/51036164/961f0b84-f25e-4fcc-8670-c327514ade0f/Stellar_analyticss.ipynb-Colab.pdf


