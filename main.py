import re
from bs4 import BeautifulSoup

with open('website.html', 'r', encoding='utf-8') as file:
    content = file.read()
soup = BeautifulSoup(content, 'html.parser')

movie_titles = [(re.sub(r'\s{2,}', r' ', element.get_text())) for element in soup.find_all(name='h3', class_='title')][::-1]

print(movie_titles)

with open('movies.txt', 'w') as file:
    for movie in movie_titles:
        file.write(movie + '\n')