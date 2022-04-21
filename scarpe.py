from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
from sklearn.metrics import balanced_accuracy_score

s = HTMLSession()
url = 'https://ingatlan.com/lista/elado+lakas+budapest/'
headers = {'User-Agent':'Mozilla/5.0'}

def getdata(url):
	max_pages = 2
	current_page = 1
	tablelist = []
	while current_page <= max_pages:
		current_url = f'{url}?page={current_page}'

		raw_html = requests.get(current_url, headers=headers)
		soup = BeautifulSoup(raw_html.text, 'html.parser')

		for entry in soup.find_all('a', {'class':'listing__link js-listing-active-area'}):
			price = entry.find('div', {'class':'price'}).text.strip()
			address = entry.find('div', {'class':'listing__address'}).text.strip()
			size = entry.find('div', {'class':'listing__parameter listing__data--area-size'}).text.strip()
			rooms = entry.find('div', {'class':'listing__parameter listing__data--room-count'}).text.strip()
			if entry.find('div', {'class':'listing__parameter listing__data--balcony-size'}):
				balcony = entry.find('div', {'class':'listing__parameter listing__data--balcony-size'}).text.strip()
			else:
				balcony = "nincs"

			print(f'Price: {price} | Address: {address} | Size: {size} | Rooms: {rooms} | Balcony: {balcony}')
			parameterek = {'Price': price, 'Address': address, 'Size': size, 'Rooms': rooms, 'Balcony': balcony}
			tablelist.append(parameterek)
		time.sleep(5)
		current_page += 1
	return tablelist


data = getdata(url)
df = pd.DataFrame(data)
df.to_csv('housing.csv')