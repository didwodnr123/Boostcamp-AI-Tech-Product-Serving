import streamlit as st
from confirm_button_hack import cache_on_button_press
import requests
import time
import pandas as pd


st.set_page_config(layout='wide')
st.header('Hello AI-it!!')

st.title('Malicious Comments Collecting Service')


def main():
    st.write('hello')
    keyword = st.text_input('Keyword you want to collect!!')
    if keyword:
        with st.spinner('Collecting Evidence...'):
            response = requests.get('http://49.50.174.246:2227/get_sample/' + keyword)
        st.success('Done!')
        
        st.markdown("<h2 style='text-align: center'>Report</h1>", unsafe_allow_html=True)
        st.markdown('-----------------------')
        st.markdown('#### Label Description')
        st.markdown('- **Hate**     : 혐오적인 표현')
        st.markdown('- **Offensive**: 공격적인 표현')
        st.markdown('-----------------------')
        
        for i, res in enumerate(response.json()):
            st.subheader(f'Evidence:{i+1}')
            st.write(res)


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