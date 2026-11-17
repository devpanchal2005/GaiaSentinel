# 🌍 GaiaSentinel - Watching Earth, Detecting Waste

A computer vision application for automated litter detection using YOLOv8 and the [TACO dataset](http://tacodataset.org/). Built with Streamlit and deployable on Streamlit Community Cloud.

---

## 🧠 What It Does

GaiaSentinel uses a pretrained **YOLOv8s** model trained on the TACO (Trash Annotations in Context) dataset to detect **all 60 TACO litter categories** in the wild, including bottles, caps, cans, cartons, cups, wrappers, bags, cigarettes and more.

| Capability | Details |
|---|---|
| 🔍 Detection | Bounding box detection with confidence scores |
| 🏷️ Classification | 60 TACO litter categories |
| 📸 Input | Image upload (JPG, PNG, JPEG) |
| ⚡ Speed | CPU inference, suitable for cloud deployment |

---

## 🤖 Model

- **Architecture:** YOLOv8s (Ultralytics)
- **Classes:** all 60 TACO categories
- **Weights:** `taco_yolov8s.pt`, trained on TACO for 100 epochs
- **Best validation scores:**
| Metric | Value |
|---|---|
| mAP50 | 0.141 |
| mAP50-95 | 0.110 |

Scores are modest because TACO has 60 fine-grained classes, many with few examples, so rare categories are often missed or mislabeled.

---

## 🗂️ Project Structure

```
GaiaSentinel/
├── app.py                 # Main Streamlit entry point & navigation
├── taco_yolov8s.pt        # Pretrained YOLOv8s weights (60 TACO classes)
├── requirements.txt       # Python dependencies
├── packages.txt           # System packages for Streamlit Community Cloud
├── assets/                # Sample images & logo
├── pages/
│   ├── Welcome.py         # Home page with the list of detected categories
│   ├── Detect_Trash.py    # Core detection interface
│   ├── What_We_Did.py     # How it works: model, scores and app flow
└── .streamlit/
    └── config.toml        # Theme & logger configuration
```

---

## 🖥️ Running Locally

### 1. Clone the repo

```bash
git clone https://github.com/devpanchal2005/GaiaSentinel.git
cd GaiaSentinel
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

The pretrained weights (`taco_yolov8s.pt`) are already included in the repo.

---

## 🚀 What's Next

- **Fine-tuning** on additional local litter photos to improve accuracy
- **Geolocation tagging** to map trash density by area
- **Recyclability classification** mapping detections to recyclable, non-recyclable or hazardous
- **Video & drone support** for monitoring public spaces over time

---

## 🙏 Credits

- **TACO Dataset** by Pedro Proença and Pedro Simões: [tacodataset.org](http://tacodataset.org)

  > Proença, P.F. and Simões, P., 2020. TACO: Trash annotations in context for litter detection. arXiv preprint arXiv:2003.06975.


---

## 📄 License

This project is for educational and research purposes. TACO dataset usage is subject to its own license terms.
