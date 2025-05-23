## Notebook Descriptions

compare_countries.ipynb
Analysis: Compare the average GHI (Global Horizontal Irradiance) across different countries.
Key Observations: Benin has the highest GHI median, Sierra Leone exhibits the lowest solar radiation, and the differences are statistically significant (p < 0.05).
Visualizations: Bar plot comparing average GHI across countries.

visualize_solar_radiation.ipynb

Analysis: Visualize the distribution of solar radiation across different months and countries.
Key Observations: Solar radiation patterns vary across months and countries, with some countries exhibiting higher radiation during certain months.
Visualizations: Heatmap and line plots showing solar radiation patterns.

====

# Running the Notebooks

To run the notebooks, follow these steps:

Install required dependencies: pip install -r requirements.txt
Navigate to the notebooks directory: cd notebooks
Run the notebook: jupyter notebook compare_countries.ipynb (or any other notebook you want to run)

===

# Data Requirements

Cleaned solar dataset (CSV) with the following columns:
Month
DNI (Direct Normal Irradiance)
GHI (Global Horizontal Irradiance)
DHI (Diffuse Horizontal Irradiance
