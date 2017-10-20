# This Python file uses the following encoding: utf-8

import unicodecsv as csv
import os.path
import json


def read_csv(file):
	f = open(file, 'r')
	reader = csv.reader(f)

	return list(reader)

# create link csv file
def create_link_csv():
	if not os.path.isfile('products/beautypedia/links.csv'):
		f = open('products/beautypedia/links.csv', 'w')
		writer = csv.writer(f)
		writer.writerow(['product', 'link'])
	else:
		print 'products/beautypedia/links.csv already exists...cannot create file'

# products = list of lists
def add_links(links):
	if not os.path.isfile('products/beautypedia/links.csv'):
		create_link_csv()

	f = open('products/beautypedia/links.csv', 'a')
	writer = csv.writer(f)
	writer.writerows(links)

# create product info csv file
def create_product_csv():
	if not os.path.isfile('products/beautypedia/products.csv'):
		f = open('products/beautypedia/products.csv', 'w')
		writer = csv.writer(f)
		writer.writerow(['DisplayName',
				'BrandName',
				'SkinType',
				'SkinConcern',
				'Ingredients',
				'Price',
				'Size',
				'BeautypediaUri',
				'AffiliateName',
				'AffiliateUri',
				'JarPackaging',
				'TestedOnAnimals',
				'CosmeticsCopReview',
				'Claims',
				'Texture',
				'Categories',
				'NumberOfFavorites',
				'NumberOfCommunityReviews',
				'CommunityRating',
				'Rating',
				'DateLastUpdated',
				'DatePublished',
				'IsBestOfTheBest',
				'ImageUrl',
				'IsAvailable'])
	else:
		print 'products/beautypedia/products.csv already exists...cannot create file'

def add_product(product):
	if not os.path.isfile('products/beautypedia/products.csv'):
		create_product_csv()

	f = open('products/beautypedia/products.csv', 'a')
	header = ['DisplayName',
				'BrandName',
				'SkinType',
				'SkinConcern',
				'Ingredients',
				'Price',
				'Size',
				'BeautypediaUri',
				'AffiliateName',
				'AffiliateUri',
				'JarPackaging',
				'TestedOnAnimals',
				'CosmeticsCopReview',
				'Claims',
				'Texture',
				'Categories',
				'NumberOfFavorites',
				'NumberOfCommunityReviews',
				'CommunityRating',
				'Rating',
				'DateLastUpdated',
				'DatePublished',
				'IsBestOfTheBest',
				'ImageUrl',
				'IsAvailable']
	dict_writer = csv.DictWriter(f, header, extrasaction='ignore')
	dict_writer.writerow(product)


