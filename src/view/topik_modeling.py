import streamlit as st
import time
import pandas as pd
from tweet_fun.scraper import load_tweet
from tweet_fun import cleaning as cln

def topik_modeling():
  st.title('Pemodelan Topik Covid19')
  st.write('Pada halaman ini akan dilakuakn pemodelan topik dari 1000 data tweet terbaru '+
          'berbahahsa indonesia yang mengandung kata covid19, hal ini dilakuakn untuk '+
          '**mengetahui topik bembahasan apa saja yang sedang dibicarakan terkait covid19**')
  st.text('')
  keyword = 'covid19'
  if st.button("Start Analysis"):
    with st.spinner('Scarping Data...'):
      df = pd.read_csv('covidtweet.csv')
      # df = load_tweet(keyword, 1000)
    st.subheader('Raw Data')
    st.dataframe(df)


    with st.spinner('Cleaning Data...'):
      df = cln.clean_part1(df)
      df = cln.clean_part2(df)
      df = cln.clean_part3(df,keyword)
    st.subheader('Clean Data')
    st.dataframe(df)

