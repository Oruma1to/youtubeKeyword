from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from functools import reduce

my_url = input("Which youtube video are you inquiring about?")

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

keywords = page_soup.findAll("meta", {"property": "og:video:tag"})

for i in keywords:
  print(i['content'])
print("===============================")

def getlength(x1):
  str1 = x1['content']
  return len(str(str1))
  
def dosum(x1, x2):
  return x1 + x2


lengths = map(getlength, keywords)
total = reduce(dosum, lengths)



# print(keywords)
print(f"There are {len(keywords)} Keywords for this video")
print(f"There are a total of {total} characters used for keywords")