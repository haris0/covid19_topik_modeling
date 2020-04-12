import streamlit as st

def about_app():
  st.title('Tentang Aplikasi')
  st.write("""
          Aplikasi ini dibuat sebagai betuk kepedulian terhadap wabah Covid19 yang 
          sedang melanda dunia saat ini dan sebagai saran pengawalan pandemi Covid19.\n
          Dengan membuat sebuah tool untuk analisi data yang ada di tweeter sehingga dapat 
          membantu kita dalam mengetahui topik ada saja yang sedang dibicarakan di tweeter, 
          Adapun analisis yang dilakukan mencakup **Wordcount** dan **Pemodelan Topik** dengan
          algoritma Latent Dirchlect Allocation(LDA) baca lebih lanjut tentang LDA
          [disini](https://medium.com/@ranggaantok/topic-modelling-menggunakan-latent-dirchlect-allocation-3fdf979ffd05).\n
          Aplikasi ini juga dilengkapi dengan berbagai informasi tentang Covid19 baik secara Global
          maupun regional.\n\n\n
          Made with :blue_heart: by [Hari Surrisyad](https://www.linkedin.com/in/haris0/)
          """)