import streamlit as st
import yaml
from predict import get_pipeline

from confirm_button_hack import cache_on_button_press

st.set_page_config(layout='wide')
st.header('Hello AI-it!!')

st.title('Malicious Comments Classification Model')

def main():    
    st.write('Model Loading...')
    pipe = get_pipeline()
    text = st.text_input('Text or Sentence you want to classify!!')
    output = pipe(text)
    st.write(output[0])

root_password = '123'
password = st.text_input('password', type='password')

@cache_on_button_press('Authenticate')
def authenticate(password) -> bool:
    st.write(type(password))
    return password == root_password

if authenticate(password):
    st.success('You are authenticated!')
    main()
else:
    st.error('The password is invalid.')