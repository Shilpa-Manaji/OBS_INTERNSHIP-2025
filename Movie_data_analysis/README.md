# 🎬 Movie Ratings Analysis & IMDb Scraper

## 📖 Overview

This project analyzes movie ratings from the **Movie dataset** and enriches it with external IMDb ratings using web scraping. The goal is to identify top-rated movies and compare user ratings with IMDb ratings.

## 📌 Features

- 📊 **Movie Ratings Analysis**: Processes `ratings.csv` to identify the highest-rated and most-rated movies.
- 🎯 **Filtering Popular Movies**: Ensures only movies with at least **50 ratings** are considered before sorting.
- 🌍 **IMDb Scraper**: Extracts IMDb ratings for movies using their IMDb IDs from `links.csv`.
- 🔗 **Data Enrichment**: Merges **MovieLens ratings** with **IMDb data** for deeper insights and analysis.

## 📂 Dataset Files(raw_data)

- `movies.csv` - Contains movie titles and genres.
- `ratings.csv` - User ratings for different movies.
- `tags.csv` - User-generated tags for movies.
- `links.csv` - Mapping of **MovieLens movie IDs** to **IMDb** and **TMDb IDs**.

## 📂 Technology Stack

- **Programming Language :** Python 3.x
- **Data Analysis & Processing :** Pandas, NumPy
- **Statistics & Machine Learning :** SciPy
- **Web Scraping :** BeautifulSoup, Requests
- **Development Environment :** Jupyter Notebook
- **Version Control :** Git & GitHub

## 📊 Workflow

### 1️. Finding the Total Number of Ratings in the Dataset

- Load `ratings.csv` into a Pandas DataFrame.
- Use `.shape` to get the total number of rows.
- The first value of `.shape` represents the total number of ratings.
- Print the result.

### 2️. Identifying the Movie with the Highest Average Rating (with at least 50 ratings)

- Load `movies.csv` and `ratings.csv` into separate DataFrames.
- Group ratings by `movieId` and calculate:
  - The count of ratings for each movie.
  - The average rating for each movie.
- Filter out movies with fewer than **50 ratings**.
- Identify the movie with the **highest average rating**.
- Retrieve the movie title using its `movieId`.
- Print the movie title.

### 3️. Determining the Most Common Rating Given by Users

- Load `ratings.csv` into a Pandas DataFrame.
- Use `.mode()` on the `rating` column to determine the most frequently occurring rating.
- Print the most common rating.

### 4️. Retrieving the IMDb Rating of the Highest-Rated Movie

- Follow the steps from **Step 2** to identify the highest-rated movie.
- Load `links.csv`, which contains IMDb IDs for movies.
- Merge the movie dataset with `links.csv` on `movieId`.
- Extract the IMDb ID of the highest-rated movie.
- Use **web scraping** to retrieve the IMDb rating (see Scraper Code below).
- Print the IMDb rating.

### 5️. Counting Sci-Fi Movies with More Than 100 Ratings

- Load `movies.csv` and `ratings.csv`.
- Merge them to have both ratings and genre information in a single DataFrame.
- Filter movies that belong to the **"Sci-Fi"** genre.
- Further filter Sci-Fi movies that have received **more than 100 ratings**.
- Count and print the number of such movies.

## 🎯 IMDb Scraper Function

```python
import requests
from bs4 import BeautifulSoup
import numpy as np

def scrapper(imdbId):
 id = str(int(imdbId))
 n_zeroes = 7 - len(id)
 new_id = "0" * n_zeroes + id
 URL = f"https://www.imdb.com/title/tt{new_id}/"
 print(f"Accessing URL: {URL}")  # Debug print

 request_header = {
 'Content-Type': 'text/html; charset=UTF-8',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)Gecko/20100101 Firefox/119.0',
 'Accept-Encoding': 'gzip, deflate, br'
 }

 response = requests.get(URL, headers=request_header)
 print(f"Response status code: {response.status_code}") # Debug print

 soup = BeautifulSoup(response.text, 'html.parser')
 imdb_rating = soup.find('span', attrs={'class': 'sc-eb51e184-1ljxVSS'})

 if imdb_rating:
     print(f"Found rating: {imdb_rating.text}")
 else:
     print("Rating not found")

 return imdb_rating.text if imdb_rating else np.nan
```

## 🛠 Example Usage

```python
imdb_rating = scrapper(111161)  # IMDb ID for "The Shawshank Redemption"
print(f"IMDb Rating: {imdb_rating}")
```

## ⚡ Prerequisites

- **Python 3.x**
- **Python Libraries**:
  - `pandas`
  - `numpy`
  - `scipy`

```bash
pip install pandas numpy scipy
```

Ensure you have the necessary dependencies installed before running the project.

## 📚 Setup Instructions

**Follow these steps to get the project up and running:**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ Shilpa-Manaji/Movie_data_analysis.git
   cd Movie_data_analysis
   ```

2. **Directory Structure**

   Your project should have the following structure:

   ```
   OBS_INTERNSHIP-2025/
   ├── Movie_data_analysis/
   │     ├──raw_data/
   │     │  ├── movies.csv
   │     │  ├── ratings.csv
   │     │  ├── tags.csv
   │     │  └── links.csv
   │     ├── data_analysis.ipynb
   │     ├── scraper.py
   │     └── README.md
   ```

3. **Open the Jupyter Notebook**

   ```bash
   jupyter notebook
   ```

- This will open Jupyter Notebook in your browser.
- Navigate and open the `data_analysis.ipynb` file.

4. **Run the Code Cells**

   - Execute each cell sequentially to complete the analysis.

---
