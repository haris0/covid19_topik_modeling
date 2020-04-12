import gensim
from gensim.models import Phrases
from gensim import corpora, models
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary
from random import randrange

def get_text_list(df):
  text = df['tweet']
  text_list =  [i.split() for i in text]

  bigram = Phrases(text_list, min_count=10)
  trigram = Phrases(bigram[text_list])
  for idx in range(len(text_list)):
    for token in bigram[text_list[idx]]:
      if '_' in token:
        text_list[idx].append(token)
    for token in trigram[text_list[idx]]:
      if '_' in token:
        text_list[idx].append(token)

  return text_list

def get_dictionary(text_list):
  dictionary = corpora.Dictionary(text_list)
  dictionary.filter_extremes(no_below=5, no_above=0.2) 
  return dictionary

def get_corpus(dictionary,text_list):
  doc_term_matrix = [dictionary.doc2bow(doc) for doc in text_list]
  tfidf = models.TfidfModel(doc_term_matrix) 
  corpus_tfidf = tfidf[doc_term_matrix]
  return corpus_tfidf

def get_topic(corpus,dictionary):
  model = LdaModel(corpus=corpus, 
                 id2word=dictionary,
                 num_topics=10) #num topic menyesuaikan hasil dari coherence value paling tinggi
  return model.print_topics()

def get_random_topik(list_alltext):
  rand_index = randrange(10)
  rand_topic = list_alltext[rand_index]
  split_topic = rand_topic.split("+")
  topic_bold = ""
  for i,string in enumerate(split_topic):
    if i == 0:
      topic_bold += "**"+string+"**"
    else:
      topic_bold += " + **"+string+"**"
  return rand_index, topic_bold