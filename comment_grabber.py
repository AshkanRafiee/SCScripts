from bs4 import BeautifulSoup, Comment
import requests
import lxml

url = 'https://ashkanrafiee.ir/main'
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
def is_comment(element): 
    return isinstance(element, Comment)
comments = soup.find_all(text=is_comment) 
for comment in comments:
    print(comment.replace('\n', '').replace('\r', '').replace('\t',''))