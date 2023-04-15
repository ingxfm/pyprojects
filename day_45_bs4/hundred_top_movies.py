from bs4 import BeautifulSoup
import requests

URL = 'https://web.archive.org/web/20200518073855/https:/www.empireonline.com/movies/features/best-movies-2/'
CLASS_LIST_ITEM: str = 'jsx-3523802742 listicle-item'
CLASS_MOVIE_NAME: str = 'jsx-4245974604'

response = requests.get(URL)
website_html = response.text
response.raise_for_status()

soup = BeautifulSoup(website_html, features='html.parser')
h3s = [title.getText() for title in soup.find_all(name='h3', class_='title',)]
reverse_order_titles = h3s[::-1]

with open('top100movies.txt', 'w') as file:
    for line in reverse_order_titles:
        file.write(f'{line}\n')
