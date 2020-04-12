# Covidian

This application was created as a concern for the Covid19 outbreak that is currently sweeping the world and as a suggestion to escort the Covid19 pandemic with data analysis. By creating tools to analyze data in tweeters so that we can help us find out what topics are being discussed in tweeters related to covid19, the analysis includes Wordcount and Topic Modeling with the Director Allocation Allocation (LDA) algorithm. This application is also equipped with various information about Covid19 both globally and regionally.

## Instaling Setup
Following this step to run the app :

- Clone this repo
- Create a virtual environment inside the folder
- Installing all requirements library using this command 
  ```
  pip install -r requirements.txt
  ```
- And App is ready to running, hit this command
  ```
  streamlit run src/app.py
  ```

## Data Apis
Source of APIs used in this application :

- [kawalcorona.com](https://kawalcorona.com/api/)
- [Pomber](https://github.com/pomber/covid19)

## Libraries
Some of the main libraries that are used in this application :

- [Twint](https://github.com/twintproject/twint)
- [Streamlit](https://streamlit.io/)