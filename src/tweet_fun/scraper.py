import twint
import streamlit as st

@st.cache
def load_tweet(keyword, limit):

  c = twint.Config()
  c.Search = keyword
  c.Limit = limit
  c.Lang = 'id'
  c.Hide_output = True
  c.Filter_retweets = True
  c.Custom["tweet"] = ['date','tweet','username']
  c.Pandas = True
  twint.run.Search(c)

  Tweets_df = twint.storage.panda.Tweets_df[['date','tweet','username']]

  return Tweets_df