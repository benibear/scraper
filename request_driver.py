import time
from random import randint
import requests

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

user_agent_list = [
		"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36"
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
		"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
		"Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0",
		"Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
		"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10"
]


def open_driver(url, classname):
	user_agent = user_agent_list[randint(0, len(user_agent_list) - 1)]
	options = webdriver.ChromeOptions()
	options.add_argument('--user-agent=' + user_agent)
	driver = webdriver.Chrome(chrome_options=options)
 
	driver.get(url)
	driver.maximize_window()
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	wait = WebDriverWait(driver, 100)
	wait.until(EC.presence_of_element_located((By.CLASS_NAME, classname)))

	soup = BeautifulSoup(driver.page_source, "html.parser")
	return soup, driver

def click_next(driver):
	driver.find_element_by_css_selector('.next-page').click()
	time.sleep(20)
	wait = WebDriverWait(driver, 100)
	wait.until(EC.presence_of_element_located((By.CLASS_NAME, "review-product")))
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	soup = BeautifulSoup(driver.page_source, "html.parser")
	return soup, driver


def get_request(url):
	time.sleep(5 + randint(0, 60))

	header = {
	    'User-Agent': user_agent_list[randint(0, len(user_agent_list) - 1)]
	}

	data = requests.get(url, headers=header)

	soup = BeautifulSoup(data.text, "html.parser")
	return soup

