#!/usr/bin/env python
#_*_ coding: utf8 _*_


import requests
import argparse


parser = argparse.ArgumentParser(description = "Headers detector")
parser.add_argument("-target",help = "Target")
parser = parser.parse_args()

if parser.target:
	try:
		url = requests.get(parser.target)
		headers = dict(url.headers)
		for i in headers:
			print("{} : {}".format(i,headers[i]))
	except:
		print("Impossible to connect")
else:
	print("No target introduced")