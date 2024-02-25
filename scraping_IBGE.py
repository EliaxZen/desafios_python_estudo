import requests
from bs4 import BeautifulSoup
import pandas as pd

def scraping_uf(uf: str) -> dict:
    uf_url = f'https://www.ibge.gov.br/cidades-e-estados/{uf}.html'
    page = requests.get(uf_url)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    indicadores = soup.select('.indicador')
    
    uf_dict = {
        dado.select('.ind-label')[0].text: dado.select('.ind-value')[0].text
        for dado in indicadores
    }
    
    return uf_dict

estado = scraping_uf('sp')


for indicador in estado:
    if ']' in estado[indicador]:
        estado[indicador] = estado[indicador].split(']')[0][:-8]
    else:
        estado[indicador] = estado[indicador]


df = pd.DataFrame(estado.values(), index=estado.keys())
print(df)




