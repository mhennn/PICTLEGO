# PICTLEGO
Do you remember the time that you build your first LEGO? Let's look back to the nostalgic and classic feeling of having a lego, feeling of Pixelated.

Introducing the PICTLEGO, a streamlit application in where you can transform your image into a pixelated or lego version within this app in a few seconds

---

### Features
- Choosing into different lego version (Disthered, Classic, Sharp)
- Easy to use, just upload the file and wait

### PICTLEGO UI
![pictlego_ui](/assets/images/streamlit_ui.png)

### Run the application
Activate the environment
```bash
py -m venv .venv
```
```bash
.venv\Scripts\activate
```

Install the dependencies
```bash
pip install -r requirements.txt
```

Run the application
```bash
streamlit run app.py
```

---
This application uses the Python Package "Legopic". In where you can transform your image into a lego style with 3 different versions and have a freedom to choose your palette.

> Image to LEGO
```bash
image = load_image(tmp_path)

palette = Palette.from_set(31203)
session = ConversionSession(
    image,
    palette,
    canvas_size=(image.width, image.height)
)

session.convert("dithered")
```

### Method for Conversion to Lego

1. Load the image
2. Setting of palette
3. Session Conversion or combining the image, palette and canvas size
4. Converting the image into different lego version
5. Save the image

---

> Check this amazing pypi project: https://pypi.org/project/legopic/?utm_source=chatgpt.com