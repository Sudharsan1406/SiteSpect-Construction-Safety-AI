import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# 1. Page Configuration
st.set_page_config(
    page_title="SiteSpect - Construction Safety Intelligence",
    page_icon="🚧",
    layout="centered"
)

st.title("🚧 SiteSpect: Construction Site Safety Intelligence")
st.write("Upload a construction site image to detect safety gear violations (Helmet, Vest, etc.) in real-time.")

# 2. Load Trained YOLO Model
@st.cache_resource
def load_model():
    model = YOLO('best.pt') 
    return model

model = load_model()

# 3. File Uploader
uploaded_file = st.file_uploader("Choose a construction site image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button('Analyze Image for Safety Gear'):
        with st.spinner('Analyzing with AI...'):
            # Run YOLO prediction
            results = model(image)
            
            # Plot the results
            res_plotted = results[0].plot()
            res_image = Image.fromarray(res_plotted[..., ::-1]) # RGB conversion
            
            st.success('Analysis Complete!')
            st.image(res_image, caption='Processed Output with Detections', use_column_width=True)