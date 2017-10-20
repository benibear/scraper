from bs4 import BeautifulSoup
import csv_writer as csv
import request_driver as rd

def save_links(soup):
	links = []
	products = soup.findAll("a", { "class" : "review-product" })

	for product in products:
		links.append([product.contents[1].encode('utf-8'), product["href"].encode('utf-8')])

	csv.add_links(links)

#returns list of strings
def link_scraper(driver=None):

	# get soup by either opening browser or advancing the page
	if not driver:
		url = "https://www.beautypedia.com/skin-care-reviews/all-skin-care-products/Skin-Care?N=4294966879+4294942732&No=0&Nrpp=96&Ns=p_date_published%7C1"
		soup, driver = rd.open_driver(url, "review-product")
	else:
		soup, driver = rd.click_next(driver) 
	
	# save links to csv file
	links = save_links(soup)
	
	# call link_scraper until you hit the last page (next_button = None)
	next_button = soup.find("div", { "class" : "next-page" })
	if next_button :
		link_scraper(driver)
	else :
		print "link scrape complete"


if __name__ == "__main__":

	link_scraper()
