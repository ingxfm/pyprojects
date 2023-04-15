# 3rd-party modules
from bs4 import BeautifulSoup

with open('website.html') as html_file:
    page_content = html_file.read()

soup = BeautifulSoup(page_content, features='html.parser')

print(soup.text)
print(soup)  # prints the html
print(soup.prettify())  # prints the html with indentations
print(f'Title: {soup.title}')
print(f'Name: {soup.title.name}')
print(f'String: {soup.title.string}')

print(soup.a)  # prints the first anchor tag only
print(soup.li)  # prints the first list item only

anchor_tags = soup.find_all(name='a')  # get by name
# print(anchor_tags)

for tag in anchor_tags:
    # print(tag)
    # print(tag.text)  # get the text
    print(tag.get('href'))  # get the links

heading = soup.find(name='h1', id='name')  # get by attribute and id combined
print(heading)


section_heading = soup.find(name='h3', class_='heading')
print(section_heading)

# using css selectors
company_url = soup.select_one(selector='p a')  # by tag or tag inside tag
print(company_url)
company_name = soup.select_one(selector='#name')  # by id
print(company_name)
company_headings = soup.select('.heading')  # by class
print(company_headings)



# this will find the attribute max_length inside the first                                                             input tag.
# form_tag = soup.find('input')
# max_length = form_tag.get("max_length")