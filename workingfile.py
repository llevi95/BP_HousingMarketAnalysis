from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests

s = HTMLSession()
url = 'https://ingatlan.com/lista/elado+lakas+budapest/'
headers = {'User-Agent':'Mozilla/5.0'}

def getdata(url):
	r = requests.get(url, headers=headers)
	soup = BeautifulSoup(r.text, 'html.parser')
	price_e = soup.find_all('div', {'class':'price'})
	prices_t = [p.get_text() for p in price_e]
	return prices_t

def getnextpage(url):
	max_pages = 12
	current_page = 1
	while current_page <= max_pages:
		current_url = print(f'{url}?page={current_page}')
		print(current_url)
				
		current_page += 1

gd = getdata(url)
np = getnextpage(url)



