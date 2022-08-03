import pandas as pd
import pyrebase
import datetime
import plotly.offline as py

from matplotlib import pyplot as plt
from fbprophet import Prophet
from fbprophet.plot import plot_plotly

import streamlit as st  # pylint: disable=import-error

NYC = "Ozone Prediction NYC"
LA = "Ozone Prediction LA"
CHICAGO = "Ozone Prediction Chicago"


# get data from firebase 

firebaseConfig = {
    "apiKey": "AIzaSyBfkHY2QHpN2T53noBDGfgpBlwCPMaMEsM",
    "authDomain": "wide-ceiling-334016.firebaseapp.com",
    "databaseURL": "https://wide-ceiling-334016-default-rtdb.firebaseio.com",
    "projectId": "wide-ceiling-334016",
    "storageBucket": "wide-ceiling-334016.appspot.com",
    "messagingSenderId": "792294632506",
    "appId": "1:792294632506:web:4d60f50e9583bed1b75903",
    "measurementId": "G-4Q0KNQVS1B"
  };

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

nyc = pd.DataFrame(db.child("AirQuality_NYC").get().val())
chicago = pd.DataFrame(db.child("AirQuality_Chicago").get().val())
la = pd.DataFrame(db.child("AirQuality_LA").get().val())

@st.cache(allow_output_mutation=True)
def make_forecast(selection):
    """Takes a name from the selection and makes a forecast plot."""

    if selection == NYC:
        data = pd.DataFrame(db.child("AirQuality_NYC").get().val())

    elif selection == CHICAGO:

        data = pd.DataFrame(db.child("AirQuality_Chicago").get().val())
        title = "Ozone Prediction Chicago"
       

    elif selection == LA:

        data = pd.DataFrame(db.child("AirQuality_LA").get().val())
        title = "Ozone Prediction LA"
       

    ##prophet_df = (
    ##    data
    ##    .diff()
    ##    .dropna()
    ##    .to_frame()
    ##    .reset_index()
    ##    .rename(columns={"date": "ds", cumulative_series_name: "y"})
    ##)
##
#    model = Prophet()
#    model.fit(prophet_df)
#    future = model.make_future_dataframe(periods=90)
#    forecast = model.predict(future)
#
#    fig = plot_plotly(model, forecast)
#    fig.update_layout(
#        title=title, yaxis_title=x_label, xaxis_title="Date",
#    )

    


    #construct future dataframe

    data['ds'] = pd.to_datetime(data['ds'])
    m = Prophet(daily_seasonality=False,weekly_seasonality=False)
    m.fit(data)
    begin_ds = data['ds'].max()
    n_future_months = 15
    month = begin_ds.month
    year = begin_ds.year
    future_dates = []
    for _ in range(n_future_months):
        month += 1
        if month > 12:
            month = 1
            year += 1
        future_dates.append(datetime.datetime(year=year,month=month,day=1))
    df_future = pd.DataFrame({'ds':future_dates})
    forecast = m.predict(df_future)

    fig = plot_plotly(m, forecast, xlabel='Month', ylabel='Ozone (ppm)')  # This returns a plotly Figure

    return fig

selected_series = st.selectbox("Select a data set:", (NYC, LA, CHICAGO))

plotly_fig = make_forecast(selected_series)
st.plotly_chart(plotly_fig)


##if selected_series == NYC:
##    cases_series = df["cumulative_cases"]
##    deaths_series = df["cumulative_deaths"]
##    recoveries_series = df["cumulative_recoveries"]
##
##    plt.title("Global Cumulative Series")
##    plt.xlabel("Date")
##    plt.ylabel("Cases")
##    plt.plot(cases_series.index, cases_series.values, label=CASES)
##    plt.plot(deaths_series.index, deaths_series.values, label=DEATHS)
##    plt.plot(recoveries_series.index, recoveries_series.values, label=RECOVERIES)
##    plt.legend()
##
##    st.pyplot()
##
##else:
##    plotly_fig = make_forecast(selected_series)
##    st.plotly_chart(plotly_fig)###