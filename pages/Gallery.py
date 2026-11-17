import json
import os
import streamlit as st

GALLERY_DIR = os.path.join("assets", "gallery")

st.set_page_config(page_title="Gallery", layout="wide")


@st.cache_data
def load_gallery():
    with open(os.path.join(GALLERY_DIR, "gallery.json"), encoding="utf-8") as f:
        return json.load(f)


st.title("🖼️ Detection Gallery")
st.markdown("""
Real-world litter photos with the boxes and labels the model draws on them.
Each label shows the predicted TACO category and its confidence score.
""")

if not os.path.exists(os.path.join(GALLERY_DIR, "gallery.json")):
    st.info("No gallery images yet.")
    st.stop()

items = load_gallery()
scenes = ["All"] + sorted({item["scene"] for item in items})
scene = st.pills("Scene", scenes, default="All") or "All"
shown = [item for item in items if scene == "All" or item["scene"] == scene]

for start in range(0, len(shown), 3):
    cols = st.columns(3)
    for col, item in zip(cols, shown[start:start + 3]):
        with col, st.container(border=True):
            st.image(os.path.join(GALLERY_DIR, item["file"]), use_container_width=True)
            st.markdown(f"**{item['caption']}**")
            st.caption(" · ".join(item["detections"]))
            licence = f" · [{item['license']}]({item['license_url']}), boxes added" if item.get("license") else ""
            st.caption(f"Photo: [{item['photographer']}]({item['url']}) on {item['source']}{licence}")
