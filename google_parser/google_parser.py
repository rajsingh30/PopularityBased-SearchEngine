import requests
from bs4 import BeautifulSoup 
def google_parser(link):
	r = requests.get(link)
	# print(r.text)
	if(r.status_code==200):
		soup=BeautifulSoup(r.text,'html.parser')
		info=soup.find_all('span',class_='st')
		link=soup.find_all('h3',class_='r')
		print(len(info))
		
		print(len(link))

google_parser('https://www.google.co.in/search?q=sunder')

