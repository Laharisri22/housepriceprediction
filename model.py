import pickle
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

# Load dataset
data = fetch_california_housing()
X = data.data
y = data.target

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved")
