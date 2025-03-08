import requests
from bs4 import BeautifulSoup

def scrapper(imdbId):
 id = str(int(imdbId))
 n_zeroes = 7 - len(id)
 new_id = "0" * n_zeroes + id
 URL = f"https://www.imdb.com/title/tt{new_id}/"
 print(f"Accessing URL: {URL}") # Debug print

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