# FIFA 21 Data Cleaning Task

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Data%20Processing-Pandas-green)](https://pandas.pydata.org/)

---

## 📌 Table of Contents

- [Objective](#-objective)
- [Key Objectives](#-Key-Objectives)
- [Technology Stack](#-technology-stack)
- [Data Cleaning Steps](#-data-cleaning-steps)
- [Usage](#-usage)

---

## 🎯 Objective

The **FIFA 21 Data Cleaning Task** aims to preprocess and refine the FIFA 21 dataset to ensure accuracy, consistency, and usability for further analysis. The raw dataset contains inconsistencies, missing values, incorrect data types, and redundant information. Cleaning this data enhances its reliability for statistical analysis and machine learning applications.

### **Why is this important?**

- **Improved Data Quality** – Ensures accuracy and consistency in player statistics.
- **Better Insights** – Enables more meaningful data analysis and visualizations.
- **Enhanced Machine Learning Performance** – Provides a solid foundation for predictive modeling.

---

## 📌 Key Objectives

1. **Handle Missing Values** – Remove or impute null/missing data.
2. **Correct Data Types** – Convert improperly formatted columns (e.g., numerical values stored as text).
3. **Remove Duplicates** – Ensure each row represents a unique player.
4. **Standardize Data** – Ensure uniform formats (e.g., currency symbols, height/weight units).
5. **Drop Irrelevant Features** – Remove unnecessary columns that don’t contribute to analysis.
6. **Fix Structural Inconsistencies** – Resolve variations in names, categories, and special characters.
7. **Detect and Handle Outliers** – Identify and address extreme values that may distort analysis.

## 📌Technology Stack

We utilize the following tools and libraries:

- **Programming Language**: [Python 3.x](https://www.python.org/)
- **Data Cleaning**: [Pandas](https://pandas.pydata.org/)
- **Version Control**: [Git](https://git-scm.com/)
- **Development Environment**: [Jupyter Notebooks](https://jupyter.org/)

---

## 📌Data Cleaning Steps

### 1. Load the Dataset

- Read the dataset from a CSV file.
- Display the first few rows to verify successful loading.
- Use `.info()` and `.describe()` to understand the structure.

### 2. Handle Missing Values

- Identify columns with missing data using `.isnull().sum()`.
- Strategies:
  - Drop columns with excessive missing data such as 'Loaned From', 'Marking'.
  - Imputed missing values with mean.

### 3. Remove Duplicates

- Detect duplicate rows using `.duplicated()`.

### 4. Convert Data Types

- Identify incorrect data types.
- Convert text-based numerical values (e.g., salaries, heights) to numeric format.
- Format categorical variables appropriately.

### 5. Standardize Formatting

- Converted height values (e.g., “5’9”) to centimeters.
- Converted weight values (e.g., “180lbs”) to kilograms.
- Standardize currency values in wage and market value columns.

### 6. Drop Unnecessary Columns

- Removed irrelevant columns such as "ID", "Flag", "Club Logo".

### 7. Fix Structural Inconsistencies

- Standardize country, club, and league names.
- Ensure consistent formatting for player positions.

### 8. Detect and Handle Outliers

- Used **Interquartile Range (IQR)** to detect extreme values.
- Choose an capping approach to handle Outliers

### 9. Validate Cleaned Data

- Recheck missing values, data types, and duplicates.
- Ensure dataset integrity for further analysis.

---

## 📌 Usage

### Prerequisites

Ensure you have Python and the required libraries installed:

```bash
pip install pandas numpy matplotlib seaborn
```

### Running the Data Cleaning Script

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Shilpa-Manaji/OBS_INTERNSHIP-2025.git
   cd fOBS_INTERNSHIP-2025
   ```

2. **Directory Structure**

   Your project should have the following structure:

   ```
   OBS_internship-2025/
   ├── FIFA21/
   │   ├──raw_data/
   │   │   └──FIFA21_official_data.csv
   │   ├── data_cleaning.ipynb
   │   ├── README.md
   ```

3. **open the Jupyterbook**

   ```
   jupyter notebook
   ```

   - This will open Jupyter Notebook in your browser.
   - Navigate and open the data_cleaning.ipynb file.

4. **Run the Code Cells**

   - Execute each cell sequentially to complete the task.

---
