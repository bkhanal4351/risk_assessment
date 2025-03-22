import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Generate synthetic dataset
data = pd.DataFrame({
    'chemical_concentration': np.random.rand(100) * 10,
    'air_quality_index': np.random.randint(50, 200, 100),
    'water_toxicity': np.random.rand(100) * 5,
    'soil_contamination': np.random.rand(100) * 2,
    'risk_level': np.random.choice(['Low', 'Moderate', 'High'], 100)
})

# Convert risk_level to numerical values
risk_mapping = {'Low': 0, 'Moderate': 1, 'High': 2}
data['risk_level'] = data['risk_level'].map(risk_mapping)

# Split dataset
X = data.drop(columns=['risk_level'])
y = data['risk_level']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
joblib.dump(model, "epa_risk_model.pkl")
