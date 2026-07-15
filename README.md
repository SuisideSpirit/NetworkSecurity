# Network Security: Phishing Data Classification Pipeline

This repository contains an end-to-end, production-grade Machine Learning pipeline designed to detect and classify phishing websites based on various network and page characteristics.

---

## 🚀 Project Overview

Phishing is a widespread cyber threat. This project implements a robust machine learning system that:
1. Extracts data from a centralized MongoDB database.
2. Performs validation checks against a predefined schema and detects data drift.
3. Cleans and transforms the features (handling missing values via KNN Imputation).
4. Trains, evaluates, and tunes multiple classification models (e.g., RandomForest, DecisionTree, LogisticRegression, GradientBoosting, AdaBoost).
5. Integrates with **MLflow** and **DagsHub** for experiment tracking and model registration.
6. Serves predictions and triggers retraining via a **FastAPI** web application.

---

## 🛠️ Technology Stack

- **Framework**: Python 3.10+
- **Machine Learning**: Scikit-Learn
- **Experiment Tracking**: MLflow, DagsHub
- **Database**: MongoDB (Atlas)
- **API Framework**: FastAPI, Uvicorn
- **Utilities**: Pandas, NumPy, YAML, PyMongo

---

## 📁 Directory Structure

```text
├── networksecurity/
│   ├── cloud/                  # Cloud sync utilities (S3 / Cloud storage integration)
│   ├── components/             # Core pipeline components
│   │   ├── data_ingestion.py   # Pulls raw data from MongoDB and splits into train/test
│   │   ├── data_validation.py  # Column check, schema validation, and drift analysis
│   │   ├── data_transformation.py # Preprocesses numerical data using KNNImputer
│   │   └── model_trainer.py    # Trains classifiers, tunes hyper-parameters, logs to MLflow
│   ├── constants/              # Centralized configuration variables & parameters
│   ├── entity/                 # Input/Output data structures (dataclasses) for pipeline steps
│   ├── exceptions/             # Custom exception handling scripts
│   ├── logging/                # Log file creation and configuration utilities
│   ├── pipeline/               # Runs the sequential components in order
│   └── utils/                  # Common helper methods (IO, grid search, model evaluation)
├── data_schema/                # Contains schema.yaml for input data validation
├── templates/                  # HTML templates for rendering tabular predictions
├── app.py                      # FastAPI server for predictions and manual training triggers
├── push_data.py                # ETL utility script to load CSV dataset into MongoDB Atlas
├── requirements.txt            # Project dependencies
├── setup.py                    # Metadata setup file to install the pipeline as a local package
└── README.md                   # Project documentation
```

---

## ⚙️ Installation & Setup

Follow these steps to run the pipeline locally:

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/NetworkSecurity.git
cd NetworkSecurity
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your credentials:
```env
MONGO_DB_URL="mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
MLFLOW_TRACKING_USERNAME="<your-dagshub-username>"
MLFLOW_TRACKING_PASSWORD="<your-dagshub-token-or-password>"
MLFLOW_TRACKING_URI="https://dagshub.com/<your-dagshub-username>/NetworkSecurity.mlflow"
```

---

## 🏃 Run the Project

### Phase 1: Push Raw Data to MongoDB
Execute `push_data.py` to extract the phishing data CSV and load it into your remote MongoDB instance:
```bash
python push_data.py
```

### Phase 2: Start the FastAPI Application
Run the web server locally using Uvicorn:
```bash
python app.py
```
Open your browser and navigate to `http://localhost:8000`.

---

## 🔌 API Endpoints

- **Swagger Documentation**: `http://localhost:8000/docs` (interactive UI to test all routes).
- **Trigger Training Pipeline**: `GET /train` — triggers the end-to-end ingestion, validation, transformation, and training pipeline.
- **Predict**: `POST /predict` — upload a custom CSV dataset of network features to generate classification predictions. The results are returned as a styled HTML table and saved to `prediction_output/output.csv`.