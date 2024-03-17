# E-Commerce Public Data Analysis with Python
![E-Commerce Data Dashboard](Sales_Dashboard.gif)

[E-Commerce Data Dashboard Streamlit App](https://sales-dashboard-k8bco2qsymea4uawg3cg4i.streamlit.app/)

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)

## Overview
This project is a data analysis and visualization project focused on e-commerce public data. It includes code for data wrangling, exploratory data analysis (EDA), and a Streamlit dashboard for interactive data exploration. This project aims to analyze data on the E-Commerce Public Dataset.

## Project Structure
- `dashboard/`: This directory contains dashboard.py which is used to create dashboards of data analysis results.
- `data/`: Directory containing the raw CSV data files.
- `notebook.ipynb`: This file is used to perform data analysis.
- `README.md`: This documentation file.

## Installation
1. Clone this repository to your local machine:
```
git clone https://github.com/azissukmawan/sales-analysis-dashboard.git
```
2. Go to the project directory
```
cd sales-analysis-dashboard
```
3. Install the required Python packages by running:
```
pip install -r requirements.txt
```

## Usage
1. **Data Wrangling**: Data wrangling scripts are available in the `notebook.ipynb` file to prepare and clean the data.

2. **Exploratory Data Analysis (EDA)**: Explore and analyze the data using the provided Python scripts. EDA insights can guide your understanding of e-commerce public data patterns.

3. **Visualization**: Run the Streamlit dashboard for interactive data exploration:

```
cd sales-analysis-dashboard/dashboard
streamlit run dashboard.py
```
Access the dashboard in your web browser at `http://localhost:8501`.

## Data Sources
The project uses E-Commerce Public Dataset from [Belajar Analisis Data dengan Python's Final Project](https://drive.google.com/file/d/1MsAjPM7oKtVfJL_wRp1qmCajtSG1mdcK/view) offered by [Dicoding](https://www.dicoding.com/).