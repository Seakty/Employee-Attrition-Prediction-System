# Employee Attrition Prediction System 👔

[![Repo](https://img.shields.io/badge/repo-Seakty/Employee--Attrition--Prediction--System-blue)](https://github.com/Seakty/Employee-Attrition-Prediction-System) [![Python](https://img.shields.io/badge/python-3.10%2B-green)](https://www.python.org) [![Streamlit](https://img.shields.io/badge/streamlit-%E2%9A%A1-orange)](https://streamlit.io/) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Professional, interactive, and easy-to-follow repository for predicting employee attrition using an XGBoost classifier and a Streamlit dashboard.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Demo](#demo)
- [Quick Start](#quick-start)
- [Model Files & Data](#model-files--data)
- [Project Structure](#project-structure)
- [GitHub & Repo Notes](#github--repo-notes)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [Security & Privacy](#security--privacy)
- [License](#license)

---

## Project Overview

This repository contains an interactive Streamlit app (`app.py`) that predicts employee attrition (whether an employee will leave) using an XGBoost classifier. The app also exposes configurable scenario inputs in the sidebar so HR analysts or product owners can explore "what-if" scenarios and estimate financial impact (replacement costs).

The app expects saved model artifacts (`champion_model.pkl` and `model_columns.pkl`) alongside the app. Training code and experiments are available in the included notebook(s).

## Key Features

- Streamlit UI for interactive scenario analysis and visualization 📊
- XGBoost binary classifier for attrition prediction
- Custom feature engineering reproduced from the notebook (e.g., `Incentive_Ratio`, `Unjustified_Stress`)
- ROI-style replacement cost estimate for decision making 💰
- Lightweight, easy to run locally or deploy to a cloud service

## Demo

### 🌐 Live Deployment

Try the app instantly online (no installation required):

**[🚀 Open Live Demo](https://employee-attrition-prediction-system-bbpmbigdiufpffkzwv5gbk.streamlit.app/)**

### Local Testing

Run locally (see Quick Start). The UI provides:
- A sidebar with employee attributes (income, incentives, level, stress, overtime, tenure, etc.)
- A gauge showing predicted attrition probability
- A simple financial impact calculator

Screenshots and GIFs are welcome — feel free to add them under `docs/` in future PRs.

## Quick Start

### Option 1: Use Live Demo (Fastest) ⚡

No setup needed — visit the live deployment:
**[🌐 Live Demo](https://employee-attrition-prediction-system-bbpmbigdiufpffkzwv5gbk.streamlit.app/)**

### Option 2: Run Locally

Prerequisites
- Python 3.10+
- `git` (to clone the repository)

Clone the repo

```bash
git clone https://github.com/Seakty/Employee-Attrition-Prediction-System.git
cd Employee-Attrition-Prediction-System/Final\ Competition
```

Create and activate a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit app

```bash
streamlit run app.py
```

Open the URL printed by Streamlit (usually `http://localhost:8501`).

## Model Files & Data

The app expects two serialized model assets in the same folder as `app.py`:

- `champion_model.pkl` — the trained XGBoost model (joblib dump) ✅
- `model_columns.pkl` — list/ordering of features used to train the model ✅

If these files are missing the app will show an error message and instructions to generate them from the notebook.

How to save model artifacts from a training script or notebook

```python
import joblib
# `model` = trained scikit-learn/XGBoost pipeline
# `model_cols` = list(model_feature_order)
joblib.dump(model, 'champion_model.pkl')
joblib.dump(model_cols, 'model_columns.pkl')
```

Data
- A sample dataset is included at `dataset/data.csv` (for reference). Do NOT commit sensitive production data to the repository.

## Project Structure

- `app.py` — Streamlit app (main entrypoint)
- `requirements.txt` — Python dependencies
- `dataset/` — example data files used for development
- `25ITC_SSeakty.ipynb` — notebook with EDA / training / model export logic
- `competition/` — other notebooks & inputs

## GitHub & Repo Notes

- Repo: https://github.com/Seakty/Employee-Attrition-Prediction-System
- Recommended branch strategy: `main` for stable, feature branches for work-in-progress.

.gitignore recommendations (do NOT commit large binaries or secrets):

```
# Byte-compiled / caches
__pycache__/
*.py[cod]

# Virtualenv
.venv/

# Model artifacts and large data (add them locally, not to repo if private)
*.pkl
dataset/*.csv

# OS files
.DS_Store
Thumbs.db
```

If your use-case requires committing a model for reproducibility, add a clear README note and keep the model small.

## Contributing

Contributions are welcome. Please follow these guidelines:

1. Fork the repository and create a feature branch.
2. Open a clear PR describing the change, why it's needed, and any testing performed.
3. Keep changes focused and add unit tests where feasible.

Suggested improvements
- Add CI to run linting and tests
- Add Dockerfile for reproducible deployments
- Add GitHub Actions to publish a Streamlit deployment or Docker image

## Troubleshooting

- Error: `Model files not found` — ensure `champion_model.pkl` and `model_columns.pkl` are in the same folder as `app.py`.
- Error: dependency/version issues — create a fresh virtual environment and `pip install -r requirements.txt`.
- UI oddities — clear browser cache or run Streamlit with `--server.runOnSave true` while developing.

## Security & Privacy

- Do not commit PII or real employee data into this repository.
- If you need to share models with others, consider gated releases or private storage (S3 with restricted access).

## License

This project is intended to be permissively licensed (suggestion: MIT). Add a `LICENSE` file to the repository with your chosen license.

---

If you'd like, I can:

- Add a `LICENSE` file (MIT) now ✅
- Create a `.gitignore` file in the repo with the recommended content ✅
- Add a minimal GitHub Actions workflow to run tests and linting 🔧

Feel free to tell me which of the above you'd like me to add next.

— Developed by Seakty
