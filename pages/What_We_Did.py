import streamlit as st

st.set_page_config(page_title="How It Works", layout="wide")
st.title("🧠 How It Works")
st.markdown("---")

st.header("🎯 Problem Statement")
st.markdown("""
Improper waste disposal remains a critical environmental issue, and manual litter monitoring
is slow and inconsistent. GaiaSentinel automatically detects and labels litter in photos
using computer vision.
""")

st.header("🧠 The Model")
st.markdown("""
- **Architecture**: YOLOv8s (Ultralytics), a fast single-stage object detector.
- **Classes**: all **60 litter categories** from the TACO (Trash Annotations in Context) dataset.
- **Weights**: weights trained on TACO for 100 epochs. The app uses them as-is,
  with no further training on our side.
""")

st.header("📈 Validation Scores")
col1, col2 = st.columns(2)
col1.metric("mAP50", "0.141")
col2.metric("mAP50-95", "0.110")
st.markdown("""
These are the best validation scores of the pretrained weights. Scores are modest because TACO
has 60 fine-grained classes, many with only a handful of examples, so expect some missed or
mislabeled objects, especially for rare categories.
""")

st.header("📦 App Flow")
st.markdown("""
1. **Upload**: you upload a JPG or PNG image on the Detect page.
2. **Inference**: the model runs on the image on the CPU. It is loaded once and cached
   between requests.
3. **Results**: detected objects are drawn as labeled bounding boxes with confidence scores
   using `result.plot()`, and the annotated image is shown next to your upload.
""")
