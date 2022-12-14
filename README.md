# AirQualityApp

## How to Use

Web app can be found here: [https://air-quality-app-xl4lmy5tzq-uc.a.run.app](https://air-quality-app-xl4lmy5tzq-uc.a.run.app).

To reproduce, clone this repository and upload AirQualityApp to [Google Container Registry](https://cloud.google.com/container-registry). Then create a job on Google Cloud Run to host web app. 

## Introduction

For at risk individuals, poor air quality can cause a variety of health issues. According to the NOAA, poor air quality is responsible for an estimated more than 100,000 premature deaths in the United States each year. Costs from air pollution-related illness are estimated at $150 billion per year. An accurate forecast of air quality can help to reduce costs and improve lives.

## Data Collection & Storage

The data was taken from the EPA's [Historical Air Quality](https://console.cloud.google.com/marketplace/details/epa/historical-air-quality?filter=category:climate&project=wide-ceiling-334016) dataset on BigQuery. Ozone (O<sub>3</sub>) levels from the top 3 most populous US cities (New York, Los Angeles, and Chicago) were collected using SQL and uploaded to a Firebase database. Docker container then uploaded to Google Cloud Container Registry with Streamlit app to visualize results. 

![alt text](https://github.com/smacauda/AirQualityApp/blob/main/images/Tree%20diagrams.jpeg "Tree diagram")

## Analysis

Time series analysis was performed using Facebook Prophet. Monthly predictions for 12 months with average RMSE of <0.01. 

### NYC

![alt text](https://github.com/smacauda/AirQualityApp/blob/main/images/airquality_NYC.png "Ozone Prediction NYC")

### LA

![alt text](https://github.com/smacauda/AirQualityApp/blob/main/images/airquality_LA.png "Ozone Prediction LA")


### Chicago

![alt text](https://github.com/smacauda/AirQualityApp/blob/main/images/airquality_Chicago.png "Ozone Prediction Chicago")
