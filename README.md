# AirQualityApp

## Data Collection

The data was taken from the EPA's [Historical Air Quality](https://console.cloud.google.com/marketplace/details/epa/historical-air-quality?filter=category:climate&project=wide-ceiling-334016) dataset on BigQuery. 

## Analysis

Time series analysis was performed using Facebook Prophet. Monthly predictions for 12 months with average RMSE of <0.01. 

## Firebase

Data was collected from BigQuery and stored in a Firebase real-time database. 
