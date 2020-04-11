
import nltk
from nltk.probability import FreqDist
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud

def marge_all_text(df):
  string = []
  for t in df.tweet:
    string.append(t)
  string = pd.Series(string).str.cat(sep=' ')
  return string

def get_top15(df):
  string = marge_all_text(df)
  tokens = nltk.word_tokenize(string)
  fdist = FreqDist()
  for word in tokens:
      fdist[word.lower()] += 1

  fdist_top15 = fdist.most_common(15)
  df_top15 = pd.DataFrame(fdist_top15, columns=['words', 'count'])

  fig, ax = plt.subplots(figsize=(10, 5))

  # Plot horizontal bar graph
  df_top15.sort_values(by='count').plot.barh(x='words',
                                              y='count',
                                              ax=ax,
                                              color="blue")

  ax.set_title("Daftar 15 kata yang paling sering muncul")
  st.pyplot()
  return fdist_top15

def show_wordclound(df):
  string = marge_all_text(df)
  wordcloud = WordCloud(background_color="white").generate(string)
  plt.figure()
  plt.imshow(wordcloud, interpolation="bilinear")
  plt.axis("off")
  st.pyplot()