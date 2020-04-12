import streamlit as st

def about_app():
  st.title('Tentang Aplikasi')
  st.write("""
          Aplikasi ini dibuat sebagai bentuk kepedulian atas wabah Covid19 yang saat ini melanda dunia 
          dan sebagai saran untuk mengawal pandemi Covid19 dengan analisis data.\n
          Dengan membuat sebuah tool untuk analisi data pada twitter sehingga dapat 
          membantu kita dalam mengetahui topik apa yang sedang dibahas pada twitter terkait dengan Covid19, 
          analisis tersebut mencakup **Wordcount** dan **Pemodelan Topik** dengan
          algoritma Latent Dirchlect Allocation(LDA) baca lebih lanjut tentang LDA
          [disini](https://medium.com/@ranggaantok/topic-modelling-menggunakan-latent-dirchlect-allocation-3fdf979ffd05).\n
          Aplikasi ini juga dilengkapi dengan berbagai informasi tentang Covid19 baik secara Global
          maupun regional.\n\n\n
          Made with :blue_heart: by [Hari Surrisyad](https://www.linkedin.com/in/haris0/)
          """)