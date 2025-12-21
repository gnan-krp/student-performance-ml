import numpy as np

data = np.loadtxt("data.csv", delimiter=",", skiprows=1)

X = data[:, :2]   # hours and attendance
y = data[:, 2]    # score

X = np.c_[np.ones(X.shape[0]), X]

theta = np.linalg.inv(X.T @ X) @ X.T @ y

hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))

prediction = theta[0] + theta[1]*hours + theta[2]*attendance

print("Predicted Score:", round(prediction, 2))
