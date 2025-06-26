import pandas as pd
import matplotlib.pyplot as plt
import os

dataset_path = r"C:\Users\ADMIN\Desktop\ds class\train.csv"

if os.path.exists(dataset_path):
    dataset = pd.read_csv(dataset_path)
    if 'Sex' in dataset.columns:
        gender_data = dataset['Sex']
        gender_distribution = gender_data.value_counts()
        gender_labels = gender_distribution.index
        gender_values = gender_distribution.values
        figure = plt.figure(figsize=(10, 6))
        bars = plt.bar(gender_labels, gender_values, color=['skyblue', 'lightcoral'], width=0.5, edgecolor='black')
        plt.title("Distribution of Gender in Titanic Dataset", fontsize=16)
        plt.xlabel("Gender", fontsize=12)
        plt.ylabel("Number of Passengers", fontsize=12)
        for index, value in enumerate(gender_values):
            plt.text(index, value + 5, str(value), ha='center', fontsize=10)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    else:
        print("The column 'Sex' was not found in the dataset.")
else:
    print("The dataset file was not found at the specified path.")
