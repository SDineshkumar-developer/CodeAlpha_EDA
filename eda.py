import pandas as pd

df = pd.read_csv("students.csv")

print("Dataset:")
print(df)

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())
print("\nMedian Marks:")
print(df["Marks"].median())

print("\nStandard Deviation:")
print(df["Marks"].std())
import matplotlib.pyplot as plt

df.plot(x="Name", y="Marks", kind="bar")

plt.savefig("marks_chart.png")

print("Chart saved successfully!")
