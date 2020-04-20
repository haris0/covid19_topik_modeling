mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"hari.surrisyad@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
token = \"pk.eyJ1IjoiaGFyaXMwIiwiYSI6ImNrOTd5NXBudzAxc2ozZ3JvcDZxajd1dXQifQ.p82ei9zcSndouW9JYUlQUw\"\n\
port = $PORT\n\
" > ~/.streamlit/config.toml