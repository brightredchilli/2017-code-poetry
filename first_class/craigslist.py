import urllib
import re
from bs4 import BeautifulSoup

url = "http://www.ikea.com/us/en/catalog/categories/departments/living_room/39130/"

html = urllib.urlopen(url).read()

soup = BeautifulSoup(html, "lxml")

r = re.compile(r"^\s+", re.MULTILINE)

titles = soup.select(".productTitle")
titles = set([r.sub("", title.text) for title in titles]) # set removes duplicates

print("\n".join(titles))
