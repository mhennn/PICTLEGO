import streamlit as st
from components import ImageLego

st.markdown(
    "<h1>PICT <span style='color:red;'>LEGO 🧱</span></h1>",
    unsafe_allow_html=True
)
st.markdown("<h5>Turn your image into a pixelated lego version</h5>",
            unsafe_allow_html=True)

img_lego = ImageLego()

container = st.container(border=True)
with container:
    uploaded_img = st.file_uploader(label="Upload Image Here", key="img_uploader", type=["jpeg", "png", "jpg"])
    if st.button("LEGO NOW"):
        if uploaded_img:
            img_lego.image_conversion(uploaded_image=uploaded_img)
            st.toast("LEGO is Successful", icon="🎉")
        else:
            st.toast("No image is uploaded", icon="‼️")