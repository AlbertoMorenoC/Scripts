#!/usr/bin/env python
#_*_ coding: utf8 _*_

from Wappalyzer import WebPage, Wappalyzer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t","--target", help = "Introduce a target")
parser = parser.parse_args()

def main():
	if parser.target:
		wap = Wappalyzer.latest()
		try:
			web = WebPage.new_from_url(parser.target)
			tecnologies_detected = wap.analyze(web)
			print("Tecnologies detected")
			for tecnology in tecnologies_detected:
				print(tecnology)
		except:
			print("Impossible to connect")
	else:
		print("Introduce a target")



if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")
		exit()