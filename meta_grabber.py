import bs4
import requests
import lxml

url = 'https://ashkanrafiee.ir/main'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text,'lxml')
metaobject = soup.select('meta')
for item in metaobject:
	print (item)