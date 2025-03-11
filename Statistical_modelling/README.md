# 🎵 Statistical Modelling

## 📖 Overview

This project aims to analyze the factors influencing the popularity of music tracks on Spotify. Using statistical modeling and machine learning, we explore how different track attributes contribute to a song's popularity.

- **Objective:** Predict track popularity based on musical features.
- **Dataset:** Spotify music track dataset containing various features like danceability, energy, loudness, valence, tempo, and explicit content.

## 📌 Features

- **Quantitative Analysis:** Investigate correlations between musical features and popularity.
- **Predictive Modeling:** Train machine learning models to predict track popularity.
- **Statistical Insights:** Provide recommendations for artists and producers.

## 📂 Technology Stack

- **Programming Language :** Python 3.x
- **Data Processing & Analysis :** Pandas
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning Models :** Scikit-learn
- **Development Environment :** Jupyter Notebook
- **Version Control :** Git & GitHub

## 📊 Workflow

### 1️⃣ Load and Explore the Dataset

- Use **Pandas** to load and inspect the dataset.
- Check for missing values and data types using `.info()`.
- Drop irrelevant columns (e.g., index columns).

### 2️⃣ Handle Missing Values

- Fill categorical missing values (e.g., Track Name, Artists) with `'Unknown'`.

### 3️⃣ Exploratory Data Analysis (EDA)

- Create a **correlation matrix** to examine relationships between numerical features.
- Visualize trends with **scatter plots** (e.g., Danceability vs. Popularity).
- Analyze distribution of popularity scores with **histograms/KDE plots**.
- Segment data based on **Explicit content** and analyze its impact.

### 4️⃣ Prepare the Data for Modeling

- Convert **Explicit** feature into an integer (0 or 1).
- Select key features like **Danceability, Energy, Loudness, Valence etc.**.
- Normalize numerical features using **StandardScaler** from Scikit-learn.

### 5️⃣ Split the Data for Training & Testing

- Use `train_test_split()` to split data into **80% training and 20% testing**.

### 6️⃣ Build a Predictive Model

- Train a **Linear Regression model** using selected features.

### 7️⃣ Evaluate the Model

- Use **Mean Squared Error (MSE)** to measure prediction deviation.
- Use **R² Score** to evaluate model performance.
- Analyze model coefficients to identify most impactful features.

### 8️⃣ Generate Insights & Recommendations

- Identify **key factors** influencing track popularity.
- Provide recommendations for optimizing track attributes (e.g., energy levels).
- Suggest advanced models like **Random Forest, Decision Trees, or Neural Networks** for better accuracy.

## Prerequisites

- **Python 3.x**
- **Python Libraries**:

  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `Scikit-learn`

  ```bash
  pip install pandas scikit-learn matplotlib seaborn
  ```

### 📚 Setup Instructions for Jupyter Notebook

**Follow these steps to get the project up and running:**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/OBS_INTERNSHIP-2025.git
   cd Statistical_modelling
   ```

2. **Directory Structure**

   Your project should have the following structure:

   ```
   OBS_INTERNSHIP-2025/
   ├── Statistical_modelling/
   │   ├──raw_data/
   │   │   └──musicdata.csv
   │   ├── modeling.ipynb
   │   ├── README.md
   ```

3. **open the Jupyterbook**

   ```
   jupyter notebook
   ```

4. **Open & Execute** `modeling.ipynb` step by step

---
