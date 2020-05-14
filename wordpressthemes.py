#!/usr/bin/env python
#_*_ coding: utf8 _*_


import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser("Wordpress themes detector")
parser.add_argument("-t","--target",help = "Introduce a target")
parser = parser.parse_args()

def main():
	if parser.target:
		headers = {"User-Agent":"Mozilla Firefox Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0."}
		request = requests.get(parser.target,headers)
		bsoup = BeautifulSoup(request.text,"html5lib")
		
		for l in bsoup.find_all("link"): #link is the label we are looking for
			if("/wp-content/themes" in l.get("href")):
				themes_link = l.get("href")
				themes_link = themes_link.split("/")
				if "themes" in themes_link:
					theme = themes_link[themes_link.index("themes") + 1]
					print(theme)
	else:
		print("Invalid argument")


if __name__ == "__main__":
	try:
		main();
	except KeyboardInterrupt:
		print("Exiting...")
		exit()
