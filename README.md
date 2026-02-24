# Heart Attack Prediction System

A desktop application that predicts heart disease risk using a machine learning model, wrapped in a Tkinter GUI with patient input forms, charts, and reporting features.

## Overview

This project combines:

- A trained Logistic Regression model for binary prediction
- A desktop GUI workflow for healthcare-style data entry
- Login and registration screens backed by Firebase Authentication
- PDF report export capability

The application is intended for educational/demo use, not clinical diagnosis.

## Core Features

- User sign-up and sign-in screens
- Patient input form with validation
- Instant prediction result (risk / no risk)
- Visual graphs for selected medical features
- Save and export report functionality (PDF)
- Info screen explaining dataset feature meanings

## Machine Learning Details

- Algorithm: Logistic Regression
- Dataset: `heart.csv`
- Train/Test split: 80/20 (`test_size=0.2`, `stratify=Y`, `random_state=2`)
- Evaluation metric in training script: Accuracy score
- Training and inference logic: `backend.py`

## Tech Stack

- Python
- Tkinter (desktop GUI)
- scikit-learn
- pandas
- numpy
- matplotlib
- reportlab
- pyrebase

## Project Structure

```text
Heart-Attack-Prediction-main/
├── Login.py
├── registration.py
├── main.py
├── backend.py
├── info.py
├── heart.csv
├── Images/
├── README.md
└── LICENSE
```

## Setup Instructions

### 1) Clone repository

```bash
git clone https://github.com/yourusername/Heart-Attack-Prediction-main.git
cd Heart-Attack-Prediction-main/Heart-Attack-Prediction-main
```

### 2) Install dependencies

```bash
pip install numpy pandas scikit-learn matplotlib reportlab pyrebase4
```

### 3) Run the application

Start from login screen:

```bash
python Login.py
```

Or run the prediction app directly:

```bash
python main.py
```

## Usage Flow

1. Create account or sign in.
2. Enter patient details in the GUI.
3. Click analysis/predict action.
4. Review prediction result and generated charts.
5. Save or export report when needed.

## Important Notes

- This project is for learning and demonstration only.
- Predictions should not be used as medical advice.
- Firebase config is currently hardcoded in source files and should be moved to environment configuration for production use.

## Known Limitations

- No model retraining pipeline inside app UI
- Accuracy values are computed in code but not fully surfaced in GUI
- Limited error handling for all edge cases
- Desktop-only workflow (no web/mobile deployment)

## Suggested Improvements

- Add `requirements.txt` for one-command setup
- Add model evaluation report section in the GUI
- Add unit tests for preprocessing and prediction
- Add secure secrets handling for Firebase credentials
- Package app into executable for easier distribution

## License

See `LICENSE`.

## Author

Adnan Rahman Sayeem
