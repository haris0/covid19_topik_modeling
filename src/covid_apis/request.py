import requests
import json
import pandas as pd
from datetime import datetime
import streamlit as st

global_loc_apis = 'https://api.kawalcorona.com/'
global_confirmed = 'https://api.kawalcorona.com/positif'
global_recovered = 'https://api.kawalcorona.com/sembuh'
global_deaths = 'https://api.kawalcorona.com/meninggal'
indo_summary = 'https://api.kawalcorona.com/indonesia'
indo_data = 'https://api.kawalcorona.com/indonesia/provinsi/'
time_series = 'https://pomber.github.io/covid19/timeseries.json'

def convert_timestamp(timestamp):
  timestamp = str(timestamp)
  timestamp = timestamp[:10]
  dt_object = datetime.fromtimestamp(int(timestamp))
  return dt_object

def get_data(url):
  response = ""
  response = requests.get(url)
  return response.json()

def get_loc_df():
  data = get_data(global_loc_apis)
  df = pd.DataFrame.from_dict(pd.json_normalize(data), orient='columns')
  columns = ['lat', 'lon']
  df_loc = pd.DataFrame(columns=columns)
  df_loc['lat'] = df['attributes.Lat']
  df_loc['lon'] = df['attributes.Long_']
  df_loc = df_loc.dropna(how='any')
  df_loc = df_loc.apply(pd.to_numeric)
  return df_loc

def get_global_data():
  data = get_data(global_loc_apis)
  df = pd.DataFrame.from_dict(pd.json_normalize(data), orient='columns')
  df = df.dropna(how='any')
  columns = ['Negara', 'Konfirmasi', 'Sembuh', 'Meninggal', 'Aktif', 'Update']
  df_global = pd.DataFrame(columns=columns)
  df_global['Negara'] = df['attributes.Country_Region']
  df_global['Konfirmasi'] = df['attributes.Confirmed']
  df_global['Sembuh'] = df['attributes.Recovered']
  df_global['Meninggal'] = df['attributes.Deaths']
  df_global['Aktif'] = df['attributes.Active']
  df_global['Update'] = df['attributes.Last_Update'].apply(lambda timestamp: convert_timestamp(timestamp))
  return df_global

def get_global_summary():
  confirmed = get_data(global_confirmed)
  recovered = get_data(global_recovered)
  deaths = get_data(global_deaths)
  data = {
    'confirmed' : confirmed['value'],
    'recovered' : recovered['value'],
    'deaths' : deaths['value']
  }
  return data

def get_indo_summary():
  response = get_data(indo_summary)
  return response

def get_indo_data():
  data = get_data(indo_data)
  df = pd.DataFrame.from_dict(pd.json_normalize(data), orient='columns')
  df = df.dropna(how='any')
  columns = ['Provinsi', 'Konfirmasi', 'Sembuh', 'Meninggal']
  df_indo = pd.DataFrame(columns=columns)
  df_indo['Provinsi'] = df['attributes.Provinsi']
  df_indo['Konfirmasi'] = df['attributes.Kasus_Posi']
  df_indo['Sembuh'] = df['attributes.Kasus_Semb']
  df_indo['Meninggal'] = df['attributes.Kasus_Meni']
  return df_indo

def get_time_series():
  data = get_data(time_series)
  data_indo = data['Indonesia']
  df = pd.DataFrame.from_dict(pd.json_normalize(data_indo), orient='columns')
  df = df.dropna(how='any')
  # df['date'] = pd.to_datetime(df['date'])
  df.rename(columns = {'confirmed':'Positif', 'deaths':'Meninggal', 'recovered':'Sembuh'}, inplace = True)
  return df
