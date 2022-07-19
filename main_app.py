#from turtle import width
import streamlit as st
from PIL import Image
st.title('hello')
st.caption('キャプション')
image = Image.open('./data/IMG_0058.JPG')
st.image(image,width=400)