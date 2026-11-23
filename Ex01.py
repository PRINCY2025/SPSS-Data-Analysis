# Ex 1: Verify the Python Machine Learning environment
import sys
import platform
import numpy as np
import pandas as pd
import matplotlib
import sklearn

print("Python version     :", sys.version.split()[0])
print("Operating system   :", platform.system())
print("NumPy version      :", np.__version__)
print("Pandas version     :", pd.__version__)
print("Matplotlib version :", matplotlib.__version__)
print("Scikit-learn ver.  :", sklearn.__version__)

# Basic NumPy operations
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("\nMatrix A:\n", a)
print("Matrix B:\n", b)
print("A + B:\n", a + b)
print("A x B (dot product):\n", np.dot(a, b))
print("Mean of A:", a.mean(), " Std of A:", round(a.std(), 3))

# Basic Pandas operations
df = pd.DataFrame({
    "Name": ["Arun", "Divya", "Karthik", "Meena", "Rahul"],
    "Age": [21, 22, 23, 21, 24],
    "Marks": [78, 85, None, 92, 67]
})
print("\nStudent DataFrame:\n", df)
print("\nMissing values per column:\n", df.isnull().sum())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print("\nAfter filling missing marks with mean:\n", df)
print("\nSummary statistics:\n", df.describe().round(2))
