import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import covid_apis.request as rq
import matplotlib.pyplot as plt
from matplotlib import dates
from PIL import Image

def about_covid():
  st.title('Tentang Covid19')
  st.write("""
  Virus Corona atau severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) adalah 
  virus yang menyerang sistem pernapasan. Penyakit karena infeksi virus ini disebut COVID-19. 
  Virus Corona bisa menyebabkan gangguan pada sistem pernapasan, pneumonia akut, sampai kematian.
  \nSumber : [alodokter.com](https://www.alodokter.com/virus-corona)
  """)

  st.title("Data Covid Global")
  st.subheader('Persebaran Covid19 Secara Global')
  df_loc = rq.get_loc_df()
  st.map(df_loc)

  st.subheader('Live Global Data')
  global_summary = rq.get_global_summary()
  st.write("""
        Konfirmasi :\n
        > # *"""+global_summary['confirmed']+"""*\n
        Sembuh :\n
        > # *"""+global_summary['recovered']+"""*\n
        Meninggal :\n
        > # *"""+global_summary['deaths']+"""*\n
        """)
  st.subheader('Kasus Global Keseluruhan')
  global_data = rq.get_global_data()
  st.write(global_data)
  st.title("Data Covid Indonesia")

  st.subheader('Statistik Kasus Indonesia')
  with st.spinner('Get Data...'):
    time_series = rq.get_time_series()
  time_series.set_index('date', inplace=True)
  time_series = time_series.iloc[39:]

  fig, ax = plt.subplots()
  time_series.plot(kind='line', stacked=False, figsize=(12, 5))
  plt.xlabel('')
  plt.title('Statistik Covid19 di Indonesia')
  st.pyplot()

  st.subheader('Live Indonesia Data')
  indo_summar = rq.get_indo_summary()
  st.write("""
        Konfirmasi :\n
        > # *"""+str(indo_summar[0]['positif'])+"""*\n
        Sembuh :\n
        > # *"""+str(indo_summar[0]['sembuh'])+"""*\n
        Meninggal :\n
        > # *"""+str(indo_summar[0]['meninggal'])+"""*\n
        """)

  st.subheader('Kasus Indonesia Keseluruhan')
  indo_data = rq.get_indo_data()
  st.write(indo_data)
  st.title("Stay Safe Everyone")
  st.write("""
           Janngan panik dan tetap waspada, mari bantu pemerintah menekan angka 
           penyebaran pandemi ini dengan #dirumahaja, bagi kalian harus dan terpaksa
           untuk tetap beraktifitas diluar jaga kesehatan dan taati semua protokol kesehatan yang ada
           agar terhindar dari penyebaran virus ini.\n
           "**Seperti semua hal buruk di dunia, ini semua juga akan berlalu, cepat atau lambat**"(Raditya Dika)
          """)
 
  video_file = open('curves-graphic-social.mp4', 'rb')
  video_bytes = video_file.read()
  st.video(video_bytes)
  st.write('Sumber Data : [Wikipedia](https://commons.wikimedia.org/wiki/File:Covid-19-curves-graphic-social-v3.gif)')

  st.subheader('Situs Penting Terkait Covid:')
  st.write("""
            * Informasi Resmi Pemerintah Republik Indonesia [Pemerintah Indonesia](https://www.covid19.go.id)
            * Coronavirus disease (COVID-19) advice for the public [WHO](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public)
            * Daftar rumah sakit rujukan pasien virus corona [Halodoc](https://www.halodoc.com/daftar-rumah-sakit-rujukan-untuk-virus-corona)
            * Novel coronavirus (COVID-19): Hal-hal yang perlu Anda ketahui [Unicef](https://www.unicef.org/indonesia/id/coronavirus)
          """)
  st.subheader('Sumber Data :')
  st.write("[Kawal Corona API](https://kawalcorona.com/api/) dan [Pomber](https://github.com/pomber/covid19)")

  
  

  

