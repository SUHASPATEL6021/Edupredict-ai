import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

st.set_page_config(page_title="EduPredict AI", page_icon="🎓", layout="wide")
st.title("🎓 EduPredict AI")
st.caption("Student performance insights • Demonstration using synthetic data")
@st.cache_data
def data():
    rng = np.random.default_rng(42)
    n = 600
    study = rng.uniform(0.5, 9, n)
    attendance = rng.uniform(45, 100, n)
    assignments = rng.integers(1, 11, n)
    sleep = rng.uniform(4, 9, n)
    score = np.clip(12 + 4.7*study + .29*attendance + 1.6*assignments + 1.2*sleep + rng.normal(0, 6, n), 0, 100)
    return pd.DataFrame({"Study hours": study, "Attendance": attendance, "Assignments": assignments, "Sleep hours": sleep, "Exam score": score.round(1)})
df = data()
features = ["Study hours", "Attendance", "Assignments", "Sleep hours"]
X_train, X_test, y_train, y_test = train_test_split(df[features], df["Exam score"], test_size=.2, random_state=42)
model = RandomForestRegressor(n_estimators=120, random_state=42, min_samples_leaf=3).fit(X_train, y_train)
a,b,c = st.columns(3)
a.metric("Synthetic records", len(df))
b.metric("Test MAE", f"{mean_absolute_error(y_test, model.predict(X_test)):.1f} pts")
c.metric("Test R²", f"{r2_score(y_test, model.predict(X_test)):.2f}")
st.subheader("Try a prediction")
with st.form("predict"):
    col1,col2 = st.columns(2)
    study = col1.slider("Study hours/day", .5, 9., 4., .5)
    attendance = col2.slider("Attendance (%)", 45, 100, 85)
    assignments = col1.slider("Assignments completed (out of 10)", 1, 10, 8)
    sleep = col2.slider("Sleep hours/night", 4., 9., 7., .5)
    submit = st.form_submit_button("Predict score", type="primary")
if submit:
    row = pd.DataFrame([[study,attendance,assignments,sleep]],columns=features)
    st.success(f"Estimated exam score: {model.predict(row)[0]:.1f}/100")
    st.info("This estimate is illustrative, not a validated predictor of real student outcomes.")
left,right = st.columns(2)
with left:
    st.plotly_chart(px.scatter(df,x="Study hours",y="Exam score",color="Attendance",title="Study vs score"),use_container_width=True)
with right:
    imp = pd.DataFrame({"Feature":features,"Importance":model.feature_importances_})
    st.plotly_chart(px.bar(imp,x="Importance",y="Feature",orientation="h",title="Model feature importance"),use_container_width=True)
st.subheader("Sample data")
st.dataframe(df.head(30),use_container_width=True)
st.download_button("Download synthetic dataset",df.to_csv(index=False),"synthetic_students.csv","text/csv")
