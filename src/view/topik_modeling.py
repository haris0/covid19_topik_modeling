import streamlit as st
import time
import pandas as pd
from tweet_fun.scraper import load_tweet
from tweet_fun import cleaning as cln
import analytic.wordcount as wc
import analytic.topik_modelling as tm
import numpy as np


def topik_modeling():
  st.title('Analisis Tweet Covid19')
  st.write("""Pada halaman ini akan dilakuakn analsis terhadap 1000 data tweet terbaru
          berbahahsa indonesia yang mengandung kata covid19, mencakup **Wordcount**, dan **Pemodelan Topik**""")
  st.text('')
  keyword = 'covid19'
  if st.button("Start Analysis"):
    with st.spinner('Scarping Data...'):
      df = load_tweet(keyword, 1000)
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
                data covid
            """) 
    st.subheader("Wordcloud :")
    wc.show_wordclound(df)

    st.subheader("Top 15 Word :")
    top15 = wc.get_top15(df)
    st.subheader("Dengan Rincian :")
    alltop15 = ""
    for i,word in enumerate(top15):
      alltop15 += str(i+1)+" "+word[0]+" disebut sebanyak "+str(word[1])+" kali\n"
    st.write("""```\n"""+alltop15+"""```""")
    
    
    st.title('Pemodelan topik')
    st.write("""Akan dilakukan pemodelan topik untuk mengetahui topik bembahasan apa saja yang sedang 
                dibicarakan terkait covid19, hal ini dilakukan dengan **Latent Dirichlet Allocations**(LDA)
            """) 
    text_list = tm.get_text_list(df)
    dictionary = tm.get_dictionary(text_list)
    corpus = tm.get_corpus(dictionary, text_list)
    topics = tm.get_topic(corpus,dictionary)
    st.header("Hasil Pemodelan Topik dengan LDA")
    alltext1 = ""
    for idx, topic in topics:
      alltext1 += 'Topic '+str(idx+1)+' : '+ topic+'\n'
    st.write("""```\n"""+alltext1+"""```""")
    st.write("""Pada hasil topik modeling diatas setiap topik menampilkan 10 kata kunci teratas 
                yang paling berkontribusi pada topik tersebut, nilai yang ada pada setiap kata kunci 
                menyatakan tingkat berkontribusi kata kunci terhadapa suatu topik\n
            """)
    st.header("Hasil Akhir")
    alltext2 = ""
    for idx, topic in topics:
      alltext2 += 'Topic '+str(idx+1)+' : '+ cln.extract_topic(topic)+'\n'
    st.write("""```\n"""+alltext2+"""```""")
    st.write("""Dari hasil akhir diatas kita akan dapat menintrepretasikan topik apa saja
                yang terkandung dalam 1000 tweet yang mengandung kata covid
            """) 

