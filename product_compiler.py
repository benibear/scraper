import re
import json
from bs4 import BeautifulSoup
import csv_writer as csv
import request_driver as rd
# import pdb; pdb.set_trace()

def save_product(soup):
	pattern = re.compile("ReactDOM.render")
	script = soup.find('script', text=pattern).text
	product_info = re.search('(?<=\"Review\":)(.|\n)*?}', script).group().encode('utf-8')
	product_info = json.loads(product_info, strict=False)

	csv.add_product(product_info)


#returns list of strings
def product_scraper():

	links = csv.read_csv('products/beautypedia/links.csv')

	for i, link in enumerate(links):
		if i > 0 :
			url = "http://www.beautypedia.com" + link[0]
			soup = rd.get_request(url)
			save_product(soup)
			print "product {} saved".format(i)


if __name__ == "__main__":

	product_scraper()

