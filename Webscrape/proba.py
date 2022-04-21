from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import time

s = HTMLSession()
url = 'https://ingatlan.com/lista/elado+lakas+budapest/'
headers = {'User-Agent':'Mozilla/5.0'}

def getdata(url):
	max_pages = 1
	current_page = 1

	while current_page <= max_pages:
		current_url = f'{url}?page={current_page}'


		raw_html = requests.get(current_url, headers=headers)
		soup = BeautifulSoup(raw_html.text, 'html.parser')

		for entry in soup.find_all('a', {'class':'listing__link js-listing-active-area'}):
			price = entry.find('div', {'class':'price'}).text.strip()
			address = entry.find('div', {'class':'listing__address'}).text.strip()
			size = entry.find('div', {'class':'listing__parameter listing__data--area-size'}).text.strip()
			rooms = entry.find('div', {'class':'listing__parameter listing__data--room-count'}).text.strip()
			
			print(f'Price: {price} , Address: {address} . Size: {size} , Rooms: {rooms}')

		time.sleep(10)
		print('\n\n')
		current_page += 1
gdu = getdata(url)
def save_csv(gdu):
	keys = gdu[0].keys()

	with open('housing.csv', 'w') as f:
		dict_writer = csv.DirctWeiter(f, keys)
		dict_writer.writeheader(keys)
		dict.writer.witerows(gdu)
save_csv(gdu)
