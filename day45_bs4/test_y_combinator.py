# 3rd-party modules
from bs4 import BeautifulSoup
import requests


response = requests.get('https://news.ycombinator.com/news')
response_state = response.status_code
html_code = response.text

soup = BeautifulSoup(html_code, 'html.parser')

titles = [title.getText() for title in soup.find_all(name='a', class_='titlelink')]
print(titles)

links = [title.get('href') for title in soup.find_all(name='a', class_='titlelink')]
print(links)

article_upvotes = [int(upvote.getText().split()[0]) for upvote in soup.find_all(name='span', class_='score')]
max_voted = article_upvotes.index(max(article_upvotes))
#[int(upvote.get('.score').getText().strip(' points')) for upvote in soup.find_all(name='span', class_='score')]
print(article_upvotes)

print(f"Title: {titles[max_voted]}\n"
      f"Link: {links[max_voted]}")

# upvote_score = 0
# more_voted_article_index = 0
# for title in titles:
#     article_title_text = title.getText()
#     article_link = title.get('href')
#     article_votes = int(title.get('.score').getText().strip(' points'))
#     print(article_votes)
#     if article_votes > upvote_score:
#         indexing = titles.index(title)
#
# print(indexing)
# print(titles[indexing])















# single tag
# title_ = soup.find(name='a', class_='titlelink')
#
# article_title_text = title_.getText()
# article_link = title_.get("href")
# article_votes = soup.find(name='span', class_='score').getText()

# print(f"Title: {article_title_text}")
# print(f"Link: {article_link}")
# print(f"Upvotes: {article_votes}")



