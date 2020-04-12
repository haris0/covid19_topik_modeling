import re
from bs4 import BeautifulSoup
import lxml
import nltk
import io
from nltk.tokenize import WordPunctTokenizer
import pandas as pd
nltk.download()

def tweet_cleaner(text):
  tok = WordPunctTokenizer()
  pat1 = r'@[A-Za-z0-9]+'
  pat2 = r'\w+:\/\/\S+'
  pat3 = r'\W*\b\w{1,3}\b'
  pat4 = r'\S*twitter.com\S*'
  combined_pat = r'|'.join((pat1, pat2, pat3, pat4))
  soup = BeautifulSoup(text, 'lxml')
  souped = soup.get_text()
  stripped = re.sub(combined_pat, '', souped)
  try:
    clean = stripped.decode("utf-8-sig").replace(u"\ufffd", "?")
  except:
    clean = stripped
  letters_only = re.sub("[^a-zA-Z]", " ", clean)
  lower_case = letters_only.lower()
  words = tok.tokenize(lower_case)
  return (" ".join(words)).strip()

def get_norm_dic():
  norm = pd.read_csv('slang_word.csv')
  norm_dic = pd.Series(norm.formal.values,index=norm.slang).to_dict()
  return norm_dic

def word_normalize(text, norm_dic):

  text_tokenized = nltk.word_tokenize(text.lower())
  text = " ".join(word if word not in norm_dic else norm_dic[word] for word in text_tokenized)
  return text

def get_stopword(keyword):
  with io.open('stopword.txt', encoding="utf-8") as f:
    stoptext = f.read().lower()
  stopword = nltk.word_tokenize(stoptext)
  stopword.append(keyword)
  return stopword

def stopword_removal(text, stopword):
  text = ' '.join([word for word in text.split() if word not in stopword])
  return text

def clean_part1(df):
  df['tweet'] = df['tweet'].apply(lambda text: tweet_cleaner(text))
  return df

def clean_part2(df):
  norm_dic = get_norm_dic()
  df['tweet'] = df['tweet'].apply(lambda text: word_normalize(text, norm_dic))
  return df

def clean_part3(df, keyword):
  stopword = get_stopword(keyword)
  df['tweet'] = df['tweet'].apply(lambda text: stopword_removal(text, stopword))
  return df

def extract_topic(text):
  letters_only = re.sub("[^a-zA-Z+ ]", "", text)
  return letters_only

