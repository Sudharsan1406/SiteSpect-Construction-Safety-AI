# SiteSpect-Construction-Safety-AI

# 🚧 SiteSpect: Automated Construction Site Safety & Progress Intelligence System

An end-to-end Computer Vision and Data Science application designed to monitor construction site safety compliance in real-time by detecting Personal Protective Equipment (PPE) violations such as missing hard hats, safety vests, and boots.

---

## 🌟 Project Overview
Construction site accidents are a major hazard worldwide. Manual monitoring is often inconsistent and prone to human error. **SiteSpect** leverages state-of-the-art Object Detection (YOLOv8) combined with an interactive Web UI (Streamlit) to automate safety gear monitoring and improve site management.

---

## 🛠️ Tech Stack & Libraries
* **Programming Language:** Python
* **Computer Vision Model:** YOLOv8 (Ultralytics)
* **Training Platform:** Google Colab (GPU T4)
* **Web Framework / UI:** Streamlit
* **Image Processing:** OpenCV, PIL, NumPy, Pandas

---

## 🚀 Key Features
1. **Real-time PPE Detection:** Accurately detects construction workers and checks for mandatory safety gear (Helmets, Safety Vests).
2. **Interactive Web App:** Users can upload site images and instantly view bounding boxes and violation analysis.
3. **Domain-Driven Solution:** Combines practical industrial safety workflows with modern AI engineering.

---

## 📂 Project Directory Structure
```text
SiteSpect-Construction-Safety-AI/
│
├── app.py                # Streamlit Web Application
├── best.pt               # Trained YOLOv8 Custom Model Weights
├── requirements.txt      # Required Python packages
└── README.md             # Project Documentation



💡 Future Enhancements
Integrating CCTV live-stream video feed support for automated alerts.

Building a predictive analytics dashboard using historical violation data.

👨‍💻 Author
SUDHARSAN M S
