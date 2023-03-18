import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import json



# @st.experimental_memo
CO2_yearly_path = "data/CO2_simplified_by_name.xlsx"
df = pd.read_excel(CO2_yearly_path)

# @st.experimental_memo
# CO2_region_path = "/Users/anna/code/L-Fandangle042/CO2_Emission_Indicator/data/carbon_dioxide/CO2_region.xlsx"
# df_region = pd.read_excel(CO2_region_path)

st.header("Welcome to the CO2 Emissions predictor")
st.text("Select a country on the sidebar and click 'Predict' 🚀")

# Country filter
st.sidebar.title("Filters")
countries_list = df['country'].unique()
country_selected = st.sidebar.selectbox("Select country", options=countries_list) #, default=countries_list)
df_selection = df.query("country == @country_selected")

# Graph
if country_selected:
    st.write('Country Selected:', country_selected)

fig = px.line(df_selection, x="year", y="CO2", color='country',
              title='CO2 emissions by country and year')
st.plotly_chart(fig, use_container_width=True)


# API implementation

url = 'http://127.0.0.1:8000/predict'
# url  = "https://co2project-vzzs3rfq7q-ew.a.run.app/predict"

if st.sidebar.button("Predict"):
    params = {"country": country_selected}
    response = requests.get(url, params=params)
    st.subheader(response)
    question = f'Will {country_selected} reach its environmental goals for CO2?: '
    st.subheader(question + response.text)
