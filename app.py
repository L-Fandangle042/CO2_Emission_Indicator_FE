import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# @st.experimental_memo
CO2_yearly_path = "/Users/anna/code/L-Fandangle042/CO2_Emission_Indicator/data/carbon_dioxide/CO2_simplified.xlsx"
df = pd.read_excel(CO2_yearly_path)

# @st.experimental_memo
CO2_region_path = "/Users/anna/code/L-Fandangle042/CO2_Emission_Indicator/data/carbon_dioxide/CO2_region.xlsx"
df_region = pd.read_excel(CO2_region_path)

st.header("CO2 Emission Indicator")

countries_list = df['country'].unique()
select_country = st.sidebar.multiselect("Select Country", options=countries_list) #, default=countries_list)

df_selection = df.query("country == @select_country")
# df_selected = df[df['country'] == select_country]

fig = px.line(df_selection, x="year", y="CO2", color='country')
st.plotly_chart(fig)



# df_selected = df[df['country'] == select_country]

# if select_country:
#     fig2 = px.line(df_selected, x="year", y="CO2")
#     st.plotly_chart(fig2)
# else:
#     st.plotly_chart(fig)

# st.write('Country Selected:', select_country)




# param1 = st.slider('Select a number', 1, 10, 3)

# param2 = st.slider('Select another number', 1, 10, 3)

# url = 'http://localhost:8080/predict'

# params = {
#     'feature1': param1,  # 0 for Sunday, 1 for Monday, ...
#     'feature2': param2
# }
# response = requests.get(url, params=params)

# st.text(response.json())
