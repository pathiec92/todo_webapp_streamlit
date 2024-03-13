import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    camara = st.camera_input("camera")
    print(camara)

if camara:
    img = Image.open(camara)
    gray_img = img.convert("L")
    st.image(gray_img)