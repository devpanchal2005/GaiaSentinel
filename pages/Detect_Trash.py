import streamlit as st
from PIL import Image
import os
import json
from PIL import ImageOps
from ultralytics import YOLO

SAMPLES_DIR = os.path.join("assets", "samples")

@st.cache_resource
def load_model():
    return YOLO("taco_yolov8s.pt")  # YOLOv8s pretrained on 60 TACO classes

@st.cache_data
def load_samples():
    with open(os.path.join(SAMPLES_DIR, "sources.json"), encoding="utf-8") as f:
        return json.load(f)

@st.cache_data
def square_thumbnail(path, size=400):
    # Center-crop to a square so the grid lines up
    return ImageOps.fit(Image.open(path).convert("RGB"), (size, size), Image.LANCZOS)

@st.cache_data
def detect_sample(path):
    # Runs on the full-size sample; result.plot() returns a BGR array
    return load_model()(Image.open(path))[0].plot()

st.title("🔍 Trash Detection")

st.markdown("""
### 💡 Tips for Best Results
- Use clear, well-lit images
- Ensure the trash item is the main subject
- Avoid cluttered backgrounds when possible
- Try different angles for better detection
""")

img = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if img:
    image = Image.open(img)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    with st.spinner("Detecting trash..."):
        model = load_model()
        result = model(image)[0]
        result_image = result.plot()
        st.image(result_image, caption="Detected Objects", use_container_width=True, channels="BGR")
else:
    st.markdown("### 🖼️ Sample Images")
    st.caption("Drag a sample into the upload box, or click Detect")

    samples = load_samples()

    selected = next((s for s in samples if s["file"] == st.session_state.get("sample_file")), None)
    if selected:
        with st.spinner("Detecting trash..."):
            result_image = detect_sample(os.path.join(SAMPLES_DIR, selected["file"]))
        st.image(result_image, channels="BGR", caption=f"Detected Objects: {selected['caption']}", use_container_width=True)

    for start in range(0, len(samples), 4):
        cols = st.columns(4)
        for col, sample in zip(cols, samples[start:start + 4]):
            with col:
                st.image(square_thumbnail(os.path.join(SAMPLES_DIR, sample["file"])), caption=sample["caption"], use_container_width=True)
                if st.button("Detect", key=f"detect_{sample['file']}", use_container_width=True):
                    st.session_state["sample_file"] = sample["file"]
                    st.rerun()
