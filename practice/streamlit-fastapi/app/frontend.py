import streamlit as st
from confirm_button_hack import cache_on_button_press
import requests
import time

st.set_page_config(layout='wide')
st.header('Hello AI-it!!')

st.title('Malicious Comments Collecting Service')


def main():
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)

    keyword = st.text_input('Keyword you want to collect!!')
    if keyword:
        st.write('Classifying...')
        response = requests.get('http://localhost:8000/inference/' + keyword)
        st.write(response.json())


root_password = '123'
password = st.text_input('password', type='password')


@cache_on_button_press('Authenticate')
def authenticate(password) -> bool:
    return password == root_password


if authenticate(password):
    st.success('You are authenticated!')
    main()
else:
    st.error('The password is invalid.')