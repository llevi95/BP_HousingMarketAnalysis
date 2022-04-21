from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import time
from csv import writer

s = HTMLSession()
url = 'https://ingatlan.com/lista/elado+lakas+budapest/'
headers = {'User-Agent':'Mozilla/5.0'}

def getdata(url):
	max_pages = 3
	current_page = 1

	while current_page <= max_pages:
		current_url = f'{url}?page={current_page}'


		raw_html = requests.get(current_url, headers=headers)
		soup = BeautifulSoup(raw_html.text, 'html.parser')
		with open('housing.csv', 'w', encoding='utf8', newline='') as f
			thewriter = writer(f)
			header = ['Price', 'Location', 'Size', 'Rooms']
			thewriter.writereow(header)
			for entry in soup.find_all('a', {'class':'listing__link js-listing-active-area'}):
				price = entry.find('div', {'class':'price'}).text.strip()
				address = entry.find('div', {'class':'listing__address'}).text.strip()
				size = entry.find('div', {'class':'listing__parameter listing__data--area-size'}).text.strip()
				rooms = entry.find('div', {'class':'listing__parameter listing__data--room-count'}).text.strip()
			
				info = [Price, Location, Size, Rooms]
				thewriter.writerow(info)

			time.sleep(10)
			print('\n\n')
			current_page += 1
getdata(url)