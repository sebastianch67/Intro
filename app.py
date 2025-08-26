import streamlit as st
from PIL import Image
st.title("App Robot")
image= Image.open('C900_07-26.jpg')
st.image(image, caption='Robot Ufactory Lite 6')

