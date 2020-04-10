import streamlit as st
from view.topik_modeling import topik_modeling
from view.about_covid import about_covid
from view.about_app import about_app

def main():
  st.sidebar.title("App Mode")
  app_mode = st.sidebar.selectbox("Pilih Halaman",
    ["Pemodelan Topik Covid19", "Tentang Covid19", "Tentang App"])
  if app_mode == "Pemodelan Topik Covid19":
    topik_modeling()
  elif app_mode == "Tentang Covid19":
    about_covid()
  elif app_mode == "Tentang App":
    about_app()

if __name__ == "__main__":
    main()