import streamlit as st
from PIL import Image
import io
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
def detect(data):
    # Same path for uploads and samples; result.plot() returns a BGR array
    return load_model()(Image.open(io.BytesIO(data)))[0].plot()

def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()

# Only one input is active at a time: an uploaded file or a selected sample
st.session_state.setdefault("uploader_key", 0)

def clear_upload():
    # Changing the key gives a fresh, empty file uploader
    st.session_state["uploader_key"] += 1

def on_upload():
    st.session_state.pop("sample_file", None)

def clear_all():
    st.session_state.pop("sample_file", None)
    clear_upload()

def toggle_sample(name):
    if st.session_state.get("sample_file") == name:
        st.session_state.pop("sample_file", None)
    else:
        st.session_state["sample_file"] = name
        clear_upload()

st.title("🔍 Trash Detection")

st.markdown("""
### 💡 Tips for Best Results
- Use clear, well-lit images
- Ensure the trash item is the main subject
- Avoid cluttered backgrounds when possible
- Try different angles for better detection
""")

img = st.file_uploader(
    "Upload an image", type=["jpg", "jpeg", "png"],
    key=f"uploader_{st.session_state['uploader_key']}", on_change=on_upload,
)

samples = load_samples()
selected = next((s for s in samples if s["file"] == st.session_state.get("sample_file")), None)

# Work out the single active input
if img:
    data, label = img.getvalue(), "Your upload"
elif selected:
    data, label = read_bytes(os.path.join(SAMPLES_DIR, selected["file"])), f"Sample: {selected['caption']}"
else:
    data = None

if data:
    head_col, clear_col = st.columns([4, 1], vertical_alignment="center")
    head_col.markdown(f"### 🎯 Result · {label}")
    clear_col.button("✕ Clear", on_click=clear_all, use_container_width=True)

    in_col, out_col = st.columns(2)
    in_col.image(Image.open(io.BytesIO(data)), caption="Input", use_container_width=True)
    with out_col:
        with st.spinner("Detecting trash..."):
            result_image = detect(data)
        st.image(result_image, channels="BGR", caption="Detected Objects", use_container_width=True)
    st.markdown("---")

st.markdown("### 🖼️ Sample Images")
st.caption("Drag a sample into the upload box, or click Detect")

for start in range(0, len(samples), 4):
    cols = st.columns(4)
    for col, sample in zip(cols, samples[start:start + 4]):
        with col:
            is_selected = selected is not None and sample["file"] == selected["file"]
            st.image(square_thumbnail(os.path.join(SAMPLES_DIR, sample["file"])), caption=sample["caption"], use_container_width=True)
            st.button(
                "Selected ✓" if is_selected else "Detect",
                key=f"detect_{sample['file']}",
                type="primary" if is_selected else "secondary",
                on_click=toggle_sample, args=(sample["file"],),
                use_container_width=True,
            )
