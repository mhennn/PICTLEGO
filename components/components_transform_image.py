from legopic import ConversionSession, Palette, load_image
from PIL import Image
import numpy as np
import streamlit as st
import io
import tempfile


class ImageLego:
    def __init__(self):
        self.img = None

    def image_conversion(self, uploaded_image):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(uploaded_image.getbuffer())
            tmp_path = tmp.name

        image = load_image(tmp_path)

        palette = Palette.from_set(31203)

        session = ConversionSession(
            image,
            palette,
            canvas_size=(image.width, image.height)
        )

        session.convert("dithered")
        arr = session.canvas.to_array()

        self.img = Image.fromarray(np.uint8(arr))

        return self.save_and_download(uploaded_image)

    def save_and_download(self, uploaded_image):
        if self.img is None:
            st.error("No image to save.")
            return

        bytes_io = io.BytesIO()
        self.img.save(bytes_io, format="JPEG")
        bytes_data = bytes_io.getvalue()

        file_name = (
            uploaded_image.name
            if hasattr(uploaded_image, "name")
            else "lego_image.jpeg"
        )

        st.download_button(
            label="Download LEGO Image",
            data=bytes_data,
            file_name=file_name,
            mime="image/jpeg"
        )