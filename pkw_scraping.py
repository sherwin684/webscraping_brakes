import requests
from bs4 import BeautifulSoup


page = requests.get(
   url='https://proxy.scrapeops.io/v1/',
   params={
       'api_key': 'b5212c07-e71f-4a94-923e-c9c950a0dca7',
       'url': 'https://www.pkwteile.de/ersatzteil/bremsscheiben/232-gelocht-val-2?page=2',
   },
)


create a BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

find the div with class "sidebar_block_additional_filter" and data-param-id "200"
elem = soup.find(
   'div', {'class': 'sidebar_block_additional_filter', 'data-param-id': '200'})

find all the input elements within this div
inputs = elem.find_all('input')


extract the values of "Durchmesser"
dictionary = {'diameter': [input['value'] for input in inputs]}
dictionary = {'loc': [input['value'] for input in inputs2]}


element = soup.find(
   'div', {'class': 'name', 'data-param-id': '100'})
element = soup.find('span', text='Einbauseite')

Extract the value of 'Einbauseite' from the element
loc = element.find_next_sibling('span').text

Append the value to a dictionary as a list with the key 'loc'
data = {'loc': [loc]}


