#!/usr/bin/env python
#_*_ coding: utf8 _*_

import mechanize
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-f","--find",help="Introduce an argument to scan")
parser = parser.parse_args();

def main():
	if parser.find:
		bus = mechanize.Browser();
		bus.set_handle_robots(False)
		bus.set_handle_equiv(False)
		bus.addheaders = [("User-Agent","Mozilla Firefox Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0.")]
		bus.open("https://www.wikipedia.org")
		
		bus.select_form(action="//www.wikipedia.org/search-redirect.php")
		bus["search"] = parser.find
		bus.submit()
		s = BeautifulSoup(bus.response().read(),"html5lib")

		for link in s.find_all("a"):
			print(link.get("href"))

	else:
		print("No argument introduced")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")
		exit();