import requests
import re

#connect to a URL
url = 'https://ashkanrafiee.ir/main'
website = requests.get(url)

#read html code
html = website.text

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)
for items in links:
	a,b = items
	print(a)