import unittest
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class ModelTests(unittest.TestCase):
    def test_training_and_prediction(self):
        rng = np.random.default_rng(42)
        X = pd.DataFrame({"Study hours":rng.uniform(.5,9,100),"Attendance":rng.uniform(45,100,100),"Assignments":rng.integers(1,11,100),"Sleep hours":rng.uniform(4,9,100)})
        y = np.clip(12 + 4.7*X["Study hours"] + .29*X["Attendance"] + 1.6*X["Assignments"] + 1.2*X["Sleep hours"],0,100)
        train, test = train_test_split(np.arange(len(X)),test_size=.2,random_state=42)
        model = RandomForestRegressor(n_estimators=20,random_state=42).fit(X.iloc[train],y.iloc[train])
        prediction = model.predict(X.iloc[test])
        self.assertEqual(len(prediction),20)
        self.assertTrue(np.isfinite(prediction).all())
        self.assertTrue(((prediction>=0)&(prediction<=100)).all())

if __name__ == "__main__":
    unittest.main()
