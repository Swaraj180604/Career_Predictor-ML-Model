# 🚀 Career Predictor AI

An ML-powered career prediction web app built with **Streamlit**, **scikit-learn**, **Joblib**, and an **Excel dataset**.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange)
![Accuracy](https://img.shields.io/badge/Accuracy-88%25-brightgreen)

---

## 📌 Features
- Rate **12 skill dimensions** via interactive sliders
- **Random Forest** model (200 trees, 88% accuracy)
- Confidence scores for **10 tech career paths**
- **Radar chart** + **bar chart** visualisations
- Dark-themed custom HTML/CSS UI
- Model serialised with **Joblib**; dataset stored in **Excel**

---

## 📁 Project Structure

```
career_predictor/
│
├── app.py                  # Streamlit application (main UI)
├── train_model.py          # Model training script
├── create_dataset.py       # Excel dataset generator
├── career_dataset.xlsx     # Excel training dataset (1000 rows)
│
├── models/
│   ├── career_model.joblib     # Trained Random Forest pipeline
│   └── label_encoder.joblib    # Label encoder for career classes
│
├── .streamlit/
│   └── config.toml         # Streamlit theme configuration
│
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
```

---

## 🧠 ML Model Details

| Property       | Value                              |
|----------------|------------------------------------|
| Algorithm      | Random Forest Classifier           |
| Trees          | 200 estimators                     |
| Preprocessing  | StandardScaler (in Pipeline)       |
| Serialisation  | Joblib                             |
| Test Accuracy  | **88%**                            |
| CV Accuracy    | **85% ± 2.6%** (5-fold)            |
| Dataset        | Excel (.xlsx) — 1000 samples       |
| Features       | 12 skill scores (1–10)             |
| Target Classes | 10 tech career paths               |

### Career Paths Predicted
- 💻 Software Engineer
- 📊 Data Scientist
- 🌐 Web Developer
- 🛡️ Cybersecurity Analyst
- 🤖 AI/ML Engineer
- 🗄️ Database Administrator
- 🔗 Network Engineer
- 🎨 UI/UX Designer
- 📋 Product Manager
- ⚙️ DevOps Engineer

---

## ⚡ Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/career-predictor.git
cd career-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Regenerate dataset & retrain model
python create_dataset.py
python train_model.py

# 4. Run the app
streamlit run app.py
```

Open http://localhost:8501 in your browser.

---

## 🚀 Deploy on Streamlit Community Cloud

### Step 1 — Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit — Career Predictor AI"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/career-predictor.git
git push -u origin main
```

### Step 2 — Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"New app"**
3. Connect your **GitHub** account
4. Select your repository: `career-predictor`
5. Set **Main file path** to: `app.py`
6. Click **"Deploy!"**

> ✅ Streamlit Cloud auto-installs `requirements.txt` — no extra config needed.

---

## 📦 Retrain the Model

If you want to update the dataset or tweak hyperparameters:

```bash
# Re-generate Excel dataset
python create_dataset.py

# Retrain and save new Joblib models
python train_model.py

# Commit updated models
git add models/ career_dataset.xlsx
git commit -m "Retrain model"
git push
```

---

## 🛠 Tech Stack

| Layer        | Technology                    |
|--------------|-------------------------------|
| Frontend     | Streamlit + Custom HTML/CSS   |
| ML           | scikit-learn Random Forest    |
| Serialisation| Joblib                        |
| Dataset      | Excel (.xlsx) via openpyxl    |
| Charts       | Plotly                        |
| Deployment   | Streamlit Community Cloud     |
| Version ctrl | GitHub                        |

---

## 📄 License
MIT License — free to use, modify, and distribute.
