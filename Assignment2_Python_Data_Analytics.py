


import numpy as np
import pandas as pd


# Q1: Python List vs NumPy Array


print("Q1: List vs NumPy Array")

py_list = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5])


list_result = [x * 2 for x in py_list]
array_result = np_array * 2

print("Python List Result:", list_result)
print("NumPy Array Result:", array_result)


# Q2: Broadcasting in NumPy


print("\nQ2: Broadcasting Example")

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

vector = np.array([10, 20, 30])

broadcast_result = matrix + vector

print("Original Matrix:\n", matrix)
print("Vector:", vector)
print("After Broadcasting Addition:\n", broadcast_result)


# Q3: Missing Values in Pandas


print("\nQ3: Handling Missing Values")

data = {
    "A": [1, 2, np.nan, 4],
    "B": [5, np.nan, 7, 8],
    "C": [9, 10, 11, np.nan]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

print("Missing Values:\n", df.isnull())

df_filled = df.fillna(df.mean())

print("After Replacing Missing Values with Mean:\n", df_filled)


# Q4: Boolean Indexing


print("\nQ4: Boolean Indexing Example")

data2 = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [22, 25, 30, 28, 24],
    "Salary": [30000, 40000, 50000, 45000, 35000],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Experience": [1, 3, 5, 4, 2]
}

df2 = pd.DataFrame(data2)

filtered = df2[(df2["Age"] > 24) & (df2["Salary"] > 35000)]

print("Filtered Data:\n", filtered)


# Q5: groupby() Function


print("\nQ5: GroupBy Example")

data3 = {
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Salary": [50000, 40000, 60000, 55000, 45000, 65000]
}

df3 = pd.DataFrame(data3)

grouped = df3.groupby("Department")["Salary"].mean()

print("Average Salary per Department:\n", grouped)

