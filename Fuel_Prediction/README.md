# 🚗 Fuel Prediction using Auto MPG Dataset

## Overview

This project focuses on predicting the miles per gallon (MPG) of automobiles using machine learning techniques. It involves data preprocessing, feature engineering, and training a deep learning model using TensorFlow.

## Dataset

- The dataset used is **auto-mpg.csv**.
- It contains various features such as horsepower, weight, displacement, and acceleration.
- The target variable is **miles per gallon (MPG)**.

## Technology Stack

- **Programming Language:** Python 3.x
- **Data Analysis & Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn, TensorFlow
- **Visualization:** Matplotlib, Seaborn
- **Development Environment:** Jupyter Notebook

## Project Workflow

### 1. Data Loading & Exploration

- The dataset is loaded using Pandas.
- Initial exploration includes checking missing values and statistical summaries.
- Visualizations are created using Matplotlib and Seaborn.

### 2. Data Preprocessing

- Handling missing values.
- Scaling features using `StandardScaler`.
- Splitting data into training and testing sets.

### 3. Model Training

- A deep learning model is built using TensorFlow.
- The dataset is trained and evaluated based on Mean Squared Error (MSE).

### 4. Evaluation & Results

- Model performance is assessed using various metrics.
- Visualizations of loss curves.

## Prerequisites

- **Python 3.x**
- **Python Libraries**:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `tensorflow`

```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow
```

## Requirements

Ensure the following Python libraries are installed:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow
```

## Setup Instructions

**Follow these steps to get the project up and running:**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Shilpa-Manaji/OBS_INTERNSHIP-2025.git
   cd Fuel_Prediction
   ```

2. **Directory Structure**

   Your project should have the following structure:

   ```
    OBS_INTERNSHIP-2025/
    ├── Fuel_Prediction/
    │   ├── auto-mpg.csv
    │   ├── model_training.ipynb
    │   ├── README.md
   ```

3. **Open the Jupyter Notebook**

   ```bash
   jupyter notebook
   ```

- This will open Jupyter Notebook in your browser.
- Navigate and open `model_training.ipynb` file.

4. **Run the Code Cells**

   - Execute each cell sequentially to complete the training.
