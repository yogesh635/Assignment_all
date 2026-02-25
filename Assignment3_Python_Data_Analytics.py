

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1. Data Cleaning & Preprocessing


print("Loading Titanic Dataset...")
df = pd.read_csv("train.csv")   

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())


df["Age"].fillna(df["Age"].median(), inplace=True)


df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

df.drop(["Name", "Ticket", "Cabin"], axis=1, inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# 2. Univariate Analysis



plt.figure()
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.figure()
df["Age"].plot(kind="density")
plt.title("Age Density Plot")
plt.xlabel("Age")
plt.show()


plt.figure()
df["Sex"].value_counts().plot(kind="bar")
plt.title("Passenger Count by Sex")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.show()


plt.figure()
plt.boxplot(df["Fare"])
plt.title("Fare Distribution")
plt.ylabel("Fare")
plt.show()



# 3. Bivariate Analysis



plt.figure()
survival_sex = pd.crosstab(df["Sex"], df["Survived"])
survival_sex.plot(kind="bar")
plt.title("Survival Count by Sex")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.show()


plt.figure()
df.boxplot(column="Fare", by="Pclass")
plt.title("Pclass vs Fare")
plt.suptitle("")
plt.xlabel("Pclass")
plt.ylabel("Fare")
plt.show()


plt.figure()
survived = df[df["Survived"] == 1]
not_survived = df[df["Survived"] == 0]

plt.scatter(survived["Age"], survived["Fare"])
plt.scatter(not_survived["Age"], not_survived["Fare"])

plt.title("Age vs Fare (Grouped by Survival)")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

