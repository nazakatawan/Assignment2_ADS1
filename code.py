# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Define functions for reading and transposing data
def read_data_excel(excel_url, sheet_name, new_cols, countries):
    """
    Reads data from an Excel file and performs necessary preprocessing.

    Parameters:
    - excel_url (str): URL of the Excel file.
    - sheet_name (str): Name of the sheet containing data.
    - new_cols (list): List of columns to select from the data.
    - countries (list): List of countries to include in the analysis.

    Returns:
    - data_read (DataFrame): Preprocessed data.
    - data_transpose (DataFrame): Transposed data.
    """
    data_read = pd.read_excel(excel_url, sheet_name=sheet_name, skiprows=3)
    data_read = data_read[new_cols]
    data_read.set_index('Country Name', inplace=True)
    data_read = data_read.loc[countries]

    return data_read, data_read.T



# The Excel URL below indicates GDP growth (annual %)
excel_url_GDP = 'https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel'

# The Excel URL below indicates arable land (% of land area)
excel_url_arable_land = 'https://api.worldbank.org/v2/en/indicator/AG.LND.ARBL.ZS?downloadformat=excel'

# The Excel URL below indicates forest area (% of land area)
excel_url_forest_area = 'https://api.worldbank.org/v2/en/indicator/AG.LND.FRST.ZS?downloadformat=excel'

# The Excel URL below indicates Urban population growth (annual %)
excel_url_urban = 'https://api.worldbank.org/v2/en/indicator/SP.URB.GROW?downloadformat=excel'
# The Excel URL below indicates electricity production from oil, gas, and coal sources (% of total)
excel_url_electricity = 'https://api.worldbank.org/v2/en/indicator/EG.ELC.FOSL.ZS?downloadformat=excel'

# The Excel URL below indicates Agriculture, forestry, and fishing, value added (% of GDP)
excel_url_agriculture = 'https://api.worldbank.org/v2/en/indicator/NV.AGR.TOTL.ZS?downloadformat=excel'

# The Excel URL below indicates CO2 emissions (metric tons per capita)
excel_url_CO2 = 'https://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.PC?downloadformat=excel'

# Parameters for reading and transposing data
sheet_name = 'Data'
new_cols = ['Country Name', '1964', '1969', '1974', '1979', '1984','1989','1994', '1999','2004', '2009', '2014','2019','2022']
countries = ['Mexico', 'Indonesia', 'Argentina', 'Italy', 'Canada', 'Spain', 'Thailand', 'Greece', 'Sweden', 'Pakistan', 'China', 'Panama', 'Norway']

# Read and transpose arable land data
data_arable_land, data_arable_land_transpose = read_data_excel(excel_url_arable_land, sheet_name, new_cols, countries)

# Read and transpose forest area data
data_forest_area, data_forest_area_transpose = read_data_excel(excel_url_forest_area, sheet_name, new_cols, countries)

# Read and transpose GDP data
data_GDP, data_GDP_transpose = read_data_excel(excel_url_GDP, sheet_name, new_cols, countries)

# Read and transpose Urban population growth data
data_urban_read, data_urban_transpose = read_data_excel(excel_url_urban, sheet_name, new_cols, countries)

# Read and transpose electricity production data
data_electricity_read, data_electricity_transpose = read_data_excel(excel_url_electricity, sheet_name, new_cols, countries)

# Read and transpose agriculture data
data_agriculture_read, data_agriculture_transpose = read_data_excel(excel_url_agriculture, sheet_name, new_cols, countries)

# Read and transpose CO2 emissions data
data_CO2, data_CO2_transpose = read_data_excel(excel_url_CO2, sheet_name, new_cols, countries)
# The function below constructs a bar plot
def bar_plot(labels_array, width, y_data, y_label, label, title, rotation=0):
    """
    Plot a grouped bar plot.

    Parameters:
    - labels_array (array-like): X-axis labels.
    - width (float): Width of each bar group.
    - y_data (list of array-like): Y-axis data for each bar.
    - y_label (str): Y-axis label.
    - label (list): Labels for each bar group.
    - title (str): Plot title.
    - rotation (float): Rotation angle for X-axis labels.
    """
    x = np.arange(len(labels_array))
    fig, ax = plt.subplots(figsize=(8, 6), dpi=200)

    for i in range(len(y_data)):
        plt.bar(x + width * i, y_data[i], width, label=label[i])

    plt.title(title, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    plt.xlabel(None)
    plt.xticks(x + width * (len(y_data) - 1) / 2, labels_array, rotation=rotation)

    plt.legend()
    ax.tick_params(bottom=False, left=True)

    plt.show()

# Function for Multiple line plots
def multiple_plot(x_data, y_data, xlabel, ylabel, title, labels, colors):
    """
    Plot multiple line plots.

    Parameters:
    - x_data (array-like): X-axis data.
    - y_data (list of array-like): Y-axis data for each line.
    - xlabel (str): X-axis label.
    - ylabel (str): Y-axis label.
    - title (str): Plot title.
    - labels (list): Labels for each line.
    - colors (list): Colors for each line.
    """
    plt.figure(figsize=(8, 6))
    plt.title(title, fontsize=10)

    for i in range(len(y_data)):
        plt.plot(x_data, y_data[i], label=labels[i], color=colors[i])

    plt.xlabel(xlabel, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    plt.legend(bbox_to_anchor=(1.02, 1))
    plt.show()

def correlation_heatmap(data, corr, title):
    """
    Display a correlation heatmap.

    Parameters:
    - data (DataFrame): Input data.
    - corr (DataFrame): Correlation matrix.
    - title (str): Heatmap title.
    """
    plt.figure(figsize=(8, 6), dpi=200)
    plt.imshow(corr, cmap='gist_gray', interpolation='none')
    plt.colorbar()

    plt.xticks(range(len(data.columns)), data.columns, rotation=90, fontsize=10)
    plt.yticks(range(len(data.columns)), data.columns, rotation=0, fontsize=10)

    plt.title(title, fontsize=10)

    labels = corr.values
    for i in range(labels.shape[0]):
        for j in range(labels.shape[1]):
            plt.text(j, i, '{:.2f}'.format(labels[i, j]),
                     ha="center", va="center", color="white")

    plt.show()

# Plot a grouped bar plot for Agriculture, forestry, and fishing, value added (% of GDP) for fifteen countries
labels_array_agr = countries
width_agr = 0.2
y_data_agr = [
    data_agriculture_read['1964'],
    data_agriculture_read['1969'],
    data_agriculture_read['1974'],
    data_agriculture_read['1979']
]
y_label_agr = '% of GDP'
label_agr = ['Year 1964', 'Year 1969', 'Year 1974', 'Year 1979']
title_agr = 'Agriculture, fishing, and forestry, value added (% of GDP)'

# Plot the grouped bar plot for fifteen countries
bar_plot(labels_array_agr, width_agr, y_data_agr, y_label_agr, label_agr, title_agr, rotation=55)

# Plot a multiple line plot for GDP growth (annual %) for selected countries
x_data_gdp = data_GDP_transpose.index
y_data_gdp = [data_GDP_transpose[country] for country in countries]
xlabel_gdp = 'Years'
ylabel_gdp = '(%) GDP Growth'
labels_gdp = countries
colors_gdp = ['red', 'salmon', 'turquoise', 'violet', 'blue', 'crimson', 'pink', 'purple', 'yellow', 'brown', 'aqua', 'fuchsia', 'indigo', 'tangerine', 'cerulean']
title_gdp = 'Annual GDP Growth for Selected Countries (%)'

# Plot the line plots for GDP of selected countries
multiple_plot(x_data_gdp, y_data_gdp, xlabel_gdp, ylabel_gdp, title_gdp, labels_gdp, colors_gdp)

# Dataframe for Greece using selected indicators
data_Greece = {
    'Urban pop. growth': data_arable_land_transpose['Greece'],
    'Electricity production': data_electricity_transpose['Greece'],
    'Agric. forestry and Fisheries': data_agriculture_transpose['Greece'],
    'CO2 Emissions': data_CO2_transpose['Greece'],
    'Forest Area': data_forest_area_transpose['Greece'],
    'GDP Annual Growth': data_GDP_transpose['Greece']
}
df_Greece = pd.DataFrame(data_Greece)

# Display the dataframe and correlation matrix Greece
print(df_Greece)
corr_Greece = df_Greece.corr()
print(corr_Greece)

# Display the correlation heatmap for Greece
correlation_heatmap(df_Greece, corr_Greece, 'Greece')

# Dataframe for Sweden using selected indicators
data_Sweden = {
    'Urban pop. growth': data_arable_land_transpose['Sweden'],
    'Electricity production': data_electricity_transpose['Sweden'],
    'Agric. forestry and Fisheries': data_agriculture_transpose['Sweden'],
    'CO2 Emissions': data_CO2_transpose['Sweden'],
    'Forest Area': data_forest_area_transpose['Sweden'],
    'GDP Annual Growth': data_GDP_transpose['Sweden']
}
df_Sweden = pd.DataFrame(data_Sweden)

# Display the dataframe and correlation matrix Sweden
print(df_Sweden)
corr_Sweden = df_Sweden.corr()
print(corr_Sweden)
# Display the correlation heatmap for Sweden  
correlation_heatmap(df_Sweden, corr_Sweden, 'Sweden')

# Line plot for years vs. arable land and forest area
multiple_plot(data_arable_land_transpose.index, [data_arable_land_transpose[country] for country in countries],
             'Years', 'Arable Land (% of land area)',
             'Arable Land vs. Forest Area for Countries', 
             countries, ['orange', 'pink', 'cyan', 'purple', 'green', 'red', 'blue', 'yellow', 'brown', 'gray', 'teal', 'magenta', 'purple', 'orange', 'blue'])

# Plot a multiple line plot for Electricity Production (annual %) for selected countries
x_data_electricity = data_electricity_transpose.index
y_data_electricity = [data_electricity_transpose[country] for country in countries]
xlabel_electricity = 'Years'
ylabel_electricity = '(%) Electricity Production'
labels_electricity = countries
colors_electricity = ['orange', 'pink', 'cyan', 'purple', 'green', 'red', 'blue', 'yellow', 'brown', 'gray', 'teal', 'magenta', 'purple', 'orange', 'blue']
title_electricity = 'Annual (%) of Electricity Production of different Countries'

# Plot the line plots for Electricity Production of selected countries
multiple_plot(x_data_electricity, y_data_electricity, xlabel_electricity, ylabel_electricity, title_electricity, labels_electricity, colors_electricity)

# Dataframe for CO2 Emissions vs. GDP Growth for selected countries
data_CO2_GDP = {
    'CO2 Emissions': data_CO2_transpose['Greece'],
    'GDP Annual Growth': data_GDP_transpose['Greece']
}
df_CO2_GDP = pd.DataFrame(data_CO2_GDP)

# Display the dataframe and correlation matrix for CO2 Emissions vs. GDP Growth in Greece
print(df_CO2_GDP)
corr_CO2_GDP = df_CO2_GDP.corr()
print(corr_CO2_GDP)

# Display the correlation heatmap for CO2 Emissions vs. GDP Growth in Greece
correlation_heatmap(df_CO2_GDP, corr_CO2_GDP, 'CO2 Emissions vs. GDP Growth (Greece)')

# Dataframe for Urban Population Growth vs. Forest Area for selected countries
data_Urban_Forest = {
    'Urban pop. growth': data_arable_land_transpose['Greece'],
    'Forest Area': data_forest_area_transpose['Greece']
}
df_Urban_Forest = pd.DataFrame(data_Urban_Forest)

# Display the dataframe and correlation matrix for Urban Population Growth vs. Forest Area in Greece
print(df_Urban_Forest)
corr_Urban_Forest = df_Urban_Forest.corr()
print(corr_Urban_Forest)

# Display the correlation heatmap for Urban Population Growth vs. Forest Area in Greece
correlation_heatmap(df_Urban_Forest, corr_Urban_Forest, 'Urban Pop. Growth vs. Forest Area (Greece)')
