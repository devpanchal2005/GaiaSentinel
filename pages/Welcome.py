import streamlit as st
import os

st.set_page_config(page_title="GaiaSentinel", page_icon=":guardsman:", layout="wide")

# Page header
st.title("🗑️ GaiaSentinel - Watching Earth, Detecting Waste")

# Hero section
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ## About This Application
    
    GaiaSentinel uses advanced computer vision and machine learning 
    to automatically identify and classify different types of waste materials. 
    This helps in:
    
    - **♻️ Waste Sorting**: Automatically categorize trash for proper recycling
    - **🌍 Environmental Impact**: Reduce contamination in recycling streams
    - **📊 Data Analytics**: Track waste patterns and composition
    - **🎯 Education**: Learn about different waste categories
    """)

with col2:
    # You can add an image here if available
    st.image(os.path.join("assets", "taco_logo.png"), use_container_width=True)

# Features section
st.markdown("## 🚀 Key Features")

feature_cols = st.columns(2)

with feature_cols[0]:
    with st.container(border=True):
        st.markdown("""
        ### 📸 Image Detection
        - Upload images for instant classification
        - Real-time processing
        - High accuracy detection
        - Multiple format support
        """)

with feature_cols[1]:
    with st.container(border=True):
        st.markdown("""
        ### 🎯 60 TACO Litter Categories
        - Bottles, caps & lids
        - Cans, cartons & cups
        - Wrappers, bags & films
        - Cigarettes and many more
        """)

# How it works section
st.markdown("---")
st.markdown("## 🔧 How It Works")

process_cols = st.columns(4)

with process_cols[0]:
    st.markdown("""
    <div style="text-align: center;">
        <div style="font-size: 40px;">📤</div>
        <h4>1. Upload</h4>
        <p>Upload your trash image</p>
    </div>
    """, unsafe_allow_html=True)

with process_cols[1]:
    st.markdown("""
    <div style="text-align: center;">
        <div style="font-size: 40px;">🔍</div>
        <h4>2. Analyze</h4>
        <p>Model processes the image</p>
    </div>
    """, unsafe_allow_html=True)

with process_cols[2]:
    st.markdown("""
    <div style="text-align: center;">
        <div style="font-size: 40px;">🏷️</div>
        <h4>3. Classify</h4>
        <p>Identify waste category</p>
    </div>
    """, unsafe_allow_html=True)

with process_cols[3]:
    st.markdown("""
    <div style="text-align: center;">
        <div style="font-size: 40px;">📋</div>
        <h4>4. Report</h4>
        <p>Get detailed results</p>
    </div>
    """, unsafe_allow_html=True)

# Getting started section
st.markdown("---")
st.markdown("## 🎯 Getting Started")

st.markdown("""
Ready to start detecting trash? Here's how to begin:

1. **Navigate to Detection**: Use the sidebar to access the detection page
2. **Upload an Image**: Choose a clear image of waste items
3. **Get Results**: View the AI's classification and confidence scores
""")

# Detection categories section
st.markdown("---")
st.markdown("## 📈 Detection Categories")

st.markdown("""
The model detects all **60 litter categories** defined by the TACO dataset.
""")

# Class names taken from the model's names (model.names), in class ID order
TACO_CLASSES = [
    'Aluminium foil', 'Battery', 'Aluminium blister pack', 'Carded blister pack',
    'Other plastic bottle', 'Clear plastic bottle', 'Glass bottle', 'Plastic bottle cap',
    'Metal bottle cap', 'Broken glass', 'Food Can', 'Aerosol', 'Drink can', 'Toilet tube',
    'Other carton', 'Egg carton', 'Drink carton', 'Corrugated carton', 'Meal carton',
    'Pizza box', 'Paper cup', 'Disposable plastic cup', 'Foam cup', 'Glass cup',
    'Other plastic cup', 'Food waste', 'Glass jar', 'Plastic lid', 'Metal lid',
    'Other plastic', 'Magazine paper', 'Tissues', 'Wrapping paper', 'Normal paper',
    'Paper bag', 'Plastified paper bag', 'Plastic film', 'Six pack rings', 'Garbage bag',
    'Other plastic wrapper', 'Single-use carrier bag', 'Polypropylene bag', 'Crisp packet',
    'Spread tub', 'Tupperware', 'Disposable food container', 'Foam food container',
    'Other plastic container', 'Plastic gloves', 'Plastic utensils', 'Pop tab',
    'Rope & strings', 'Scrap metal', 'Shoe', 'Squeezable tube', 'Plastic straw',
    'Paper straw', 'Styrofoam piece', 'Unlabeled litter', 'Cigarette',
]

class_cols = st.columns(4)
per_col = (len(TACO_CLASSES) + len(class_cols) - 1) // len(class_cols)
for i, col in enumerate(class_cols):
    with col:
        st.markdown("\n".join(f"- {name}" for name in TACO_CLASSES[i * per_col:(i + 1) * per_col]))



