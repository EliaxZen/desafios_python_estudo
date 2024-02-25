import requests
from bs4 import BeautifulSoup

globo_url = 'https://www.globo.com/'
page = requests.get(globo_url)

resposta = page.text

soup = BeautifulSoup(resposta, 'html.parser')

noticias = soup.find_all('h2', {'class': 'post__title'})

for i in range (len(noticias)):
    print(noticias[i].text)
    
