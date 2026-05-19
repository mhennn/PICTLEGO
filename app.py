import streamlit as st
from components import ImageLego

def main():
    st.markdown(
        "<h1>PICT <span style='color:red;'>LEGO 🧱</span></h1>",
        unsafe_allow_html=True
    )
    st.markdown("<h5>Turn your image into a pixelated lego version</h5>",
                unsafe_allow_html=True)

    img_lego = ImageLego()

    container = st.container(border=True)
    with container:
        uploaded_img = st.file_uploader(label="Upload Image Here", key="img_uploader", type=["jpeg", "png", "jpg"], accept_multiple_files=False)

        convert_options = ["classic", "sharp", "dithered"]
        converted_mode = st.selectbox("Select Mode", options=convert_options, width="stretch")

        cols = st.columns(2)
        with cols[0]:
            st.image("assets/images/sample.jpg", caption="Before")
            st.image("assets/images/sharp_output.jpg", caption="Sharp")
        with cols[1]:
            st.image("assets/images/dithered_output.jpg", caption="Dithered")
            st.image("assets/images/classic_output.jpg", caption="Classic")
            

        if st.button("LEGO NOW", width="stretch"):
            if uploaded_img:
                with st.spinner(f"Building Lego of your image for {converted_mode} version..."):
                    img_lego.image_conversion(uploaded_image=uploaded_img, convert_mode=converted_mode)
                st.toast("LEGO is Successful", icon="🎉")
            else:
                st.toast("No image is uploaded", icon="‼️")

if __name__ == "__main__":
    main()