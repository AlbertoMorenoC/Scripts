#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import argparse
from os import path

parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",help = "File to upload" )
parser = parser.parse_args()


def main():
	if parser.file:
		if path.exists(parser.file):
			file = open(parser.file,"rb")
			headers = {"User-Agent":"Firefox"}
			request = requests.post(url = "https://curso--python-0-prueba-pentest1.000webhostapp.com/",files = {"uploaded_file": file},headers = headers)
			
			if parser.file in request.text:
				print(request.text)
				print("Succesfully upload")
			else:
				print("Not possible to upload the file")
		else:
			print("Not existing file")
	else:
		print("Any file to upload")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")