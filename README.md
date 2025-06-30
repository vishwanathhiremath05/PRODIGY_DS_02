
🚢 **PRODIGY_DS_02 – Titanic Gender Distribution Visualization**
This project visuaizes the gender distribution of passengers aboard the Titanic using Python. It focuses on creating a bar chart representation based on the `'Sex'` column in the dataset.

### 📁 Dataset File Used

`train.csv`
**Source:** [Kaggle – Titanic: Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic/data)

---

### 📊 Visualization

#### Gender Distribution (Bar Chart)

* Shows the number of male and female passengers on the Titanic.
* Includes value annotations on each bar for better readability.
* Gridlines and styled colors improve clarity and aesthetics.

---

### 🖼️ Sample Output

* Gender Distribution Chart (Bar Plot with Count Labels)

---

### 🚀 How to Run

#### 1. Modify Dataset Path (if needed)

Update the `dataset_path` in the script to point to the correct location of your `train.csv` file on your system.

#### 2. Install Required Libraries

```bash
pip install pandas matplotlib
```

#### 3. Run the Script

```bash
python titanic_gender_visualization.py
```

#### The script will:

✅ Load the Titanic dataset (train.csv)
✅ Extract gender data from the `'Sex'` column
✅ Plot and display the gender distribution using a customized bar chart

---

### 💡 Note

* The script checks for the file path using `os.path.exists()` for robust execution.
* Saving the plot using `plt.savefig()` is not currently implemented but can be added easily.

---

### 📧 Author

**Vishwanath Hiremath**
GitHub: [@vishwanathhiremath05](https://github.com/vishwanathhiremath05)

