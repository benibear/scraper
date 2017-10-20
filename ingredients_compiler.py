import re
import json
import os.path
from bs4 import BeautifulSoup
import csv_writer as csv_writer
import unicodecsv as csv
import request_driver as rd
# import pdb; pdb.set_trace()

def create_ingredient_csv():
	if not os.path.isfile('ingredients/ingredients_dictionary2.csv'):
		f = open('ingredients/ingredients_dictionary2.csv', 'w')
		writer = csv.writer(f)
		writer.writerow(['ingredient','rating','description'])
	else:
		print 'ingredients/ingredients_dictionary2.csv already exists...cannot create file'

def add_ingredient(ingredient):
	if not os.path.isfile('ingredients/ingredients_dictionary2.csv'):
		create_ingredient_csv()

	f = open('ingredients/ingredients_dictionary2.csv', 'a')
	dict_writer = csv.writer(f)
	dict_writer.writerow(ingredient)


def save_ingredient(soup):
	ingredient = soup.find('div', {'class': 'u-miscellaneous-pagetitle'}).find('h1').text.encode('utf-8')
	rating = soup.find('dl', {'class': 'clearfix'}).text.encode('utf-8')
	description = soup.find('div', {'class': 'upper-body'}).text.encode('utf-8')

	add_ingredient([ingredient, rating, description])


#returns list of strings
def ingredient_scraper():

	links = csv_writer.read_csv('ingredients/ingredients_links.csv')


	for i, link in enumerate(links):
		if i > 0:
			url = "http://www.paulaschoice.com" + link[0]
			soup = rd.get_request(url)
			print url
			save_ingredient(soup)
			print "ingredient {} saved".format(i)


if __name__ == "__main__":

	ingredient_scraper()


