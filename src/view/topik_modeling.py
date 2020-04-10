import streamlit as st
import time
import pandas as pd
from tweet_fun.scraper import load_tweet
from tweet_fun import cleaning as cln
import analytic.wordcount as wc
import numpy as np

# mengetahui topik bembahasan apa saja yang sedang dibicarakan terkait covid19*
def topik_modeling():
  st.title('Analisis Tweet Covid19')
  st.write("""Pada halaman ini akan dilakuakn analsis terhadap 1000 data tweet terbaru
          berbahahsa indonesia yang mengandung kata covid19, mencakup **Wordcount**, dan **Pemodelan Topik**""")
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
      df = cln.clean_part3(df,'covid')
    st.subheader('Clean Data')
    st.dataframe(df)

    st.title('Wordcount')
    st.write("""Akan dilakukan penghitungan kata, untuk mengetahui kata yang paling sering muncul
            dari 1000 data tweet, hal ini dilakuakn untuk memperkirakan keyword dalam topik pembahsan
            data covid""") 

    st.subheader("Wordcloud :")
    wc.show_wordclound(df)

    st.subheader("Top 15 Word :")
    top15 = wc.get_top15(df)
    st.subheader("Dengan Rincian :")
    for i,word in enumerate(top15):
      st.write(str(i+1)+" **"+word[0]+"** disebut sebanyak "+str(word[1])+" kali")
    

