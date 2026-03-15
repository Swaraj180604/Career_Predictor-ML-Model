import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
import joblib
import os

# ── Load dataset ──────────────────────────────────────────────────────────────
df = pd.read_excel("career_dataset.xlsx")
print(f"Dataset shape: {df.shape}")

FEATURES = ["math","logic","creativity","communication","leadership",
            "problem_solving","programming","data_analysis","design",
            "networking","management","writing"]
TARGET = "Career"

X = df[FEATURES]
y = df[TARGET]

# ── Encode labels ─────────────────────────────────────────────────────────────
le = LabelEncoder()
y_enc = le.fit_transform(y)

# ── Train / test split ────────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y_enc, test_size=0.2, random_state=42, stratify=y_enc
)

# ── Build pipeline ────────────────────────────────────────────────────────────
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("clf",    RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        min_samples_split=2,
        random_state=42,
        n_jobs=-1
    ))
])

# ── Train ─────────────────────────────────────────────────────────────────────
pipeline.fit(X_train, y_train)

# ── Evaluate ──────────────────────────────────────────────────────────────────
y_pred = pipeline.predict(X_test)
acc    = accuracy_score(y_test, y_pred)
cv     = cross_val_score(pipeline, X, y_enc, cv=5, scoring="accuracy")

print(f"\nTest Accuracy : {acc:.4f}")
print(f"CV Accuracy   : {cv.mean():.4f} ± {cv.std():.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# ── Feature importance ────────────────────────────────────────────────────────
importances = pipeline.named_steps["clf"].feature_importances_
feat_imp = pd.Series(importances, index=FEATURES).sort_values(ascending=False)
print("\nFeature Importances:")
print(feat_imp)

# ── Save artefacts ────────────────────────────────────────────────────────────
os.makedirs("models", exist_ok=True)
joblib.dump(pipeline, "models/career_model.joblib")
joblib.dump(le,       "models/label_encoder.joblib")

print("\n✅  Saved  →  models/career_model.joblib")
print("✅  Saved  →  models/label_encoder.joblib")
