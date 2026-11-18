# 🎓 EduPredict AI

Interactive student-performance prediction dashboard built with Streamlit, scikit-learn and Plotly.

## 🌐 Live demo
**[Try EduPredict AI](https://suhas-edupredict-ai.streamlit.app/)**

The public demo is hosted on Streamlit Community Cloud. The app uses synthetic data.

## Features
- Interactive input sliders and exam-score prediction
- Random forest regression model
- Holdout-set MAE and R²
- Interactive charts and feature importance
- Downloadable synthetic dataset

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Important limitation
**All training and evaluation data are synthetic.** The reported metrics are measured on held-out synthetic samples, not real students. Predictions are educational demonstrations and should not be used to make academic decisions.

## Stack
Python · Streamlit · pandas · NumPy · scikit-learn · Plotly

Created as a portfolio demonstration.
