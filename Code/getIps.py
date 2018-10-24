import requests
from bs4 import BeautifulSoup
import csv

def getProxies():
	csvfile = file('ips.csv', 'w')
	writer = csv.writer(csvfile)
	url = 'http://www.xicidaili.com/nn/'
	myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
	r = requests.get(url, headers=myheaders)
	soup = BeautifulSoup(r.text,'html.parser')
	trs = soup.find_all('tr')
	for item in trs:
		try:
			temp = []
			tds = item.find_all('td')
			temp.append(tds[1].text)
			temp.append(tds[2].text)
			writer.writerow(temp)
		except:
			pass
	return temp

getProxies()
