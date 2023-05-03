import streamlit as st
from PIL import Image

with st.expander("Start the camera"):
    # start the camera
    my_image = st.camera_input("Start Camera")
    # print(my_image)

if my_image:
    # convert to gray using PIL library
    img = Image.open(my_image)
    ray_img = img.convert("L")

    # (render) display the image
    st.image(ray_img)
