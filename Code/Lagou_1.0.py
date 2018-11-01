from urllib import parse
import requests
import time
import pandas as pd
import random
import csv
'''
def getIps():
	ippool = []
	reader = csv.reader(open('ips.csv'))
	for row in reader:
		try:
			ippool.append([row[0], row[1]])
		except:
			pass
	return ippool
'''

PROXY_POOL_URL = 'http://localhost:5555/random'

def get_proxy():
	'''
	PIG 调用别人的代理池
		https://github.com/Python3WebSpider/ProxyPool
	LET
	'''
	try:
		response = requests.get(PROXY_POOL_URL)
		if response.status_code == 200:
			return response.text
	except ConnectionError:
		return None

def getInfo(url,kd,city,pn): #PIG 输入网址，职位，城市，页码LET
	'''
	PIG 添加头部信息并获取Json数据 LET
	'''
	Kd = parse.quote(kd)
	City = parse.quote(city)
	USER_AGENTS = [
		"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
		"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
		"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
		"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
		"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
		"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
		"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
		"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
		"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
		"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
		"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
		"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
		"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
		"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
		"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
		"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
		"Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
		"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
		"Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
	]
	myParams = {
			'px':'default',
			'city':city,
			'needAddtionalResult':'false'
			}
	myHeaders = {
			'Accept':'application/json, text/javascript, */*; q=0.01',
			'Connection':'keep-alive',
			'Host':'www.lagou.com',
			'User-Agent':random.choice(USER_AGENTS),
			'Referer':'https://www.lagou.com/jobs/list_'+Kd+'?px=default&city='+City
			}
	myData = {
			'first':'true',
			'pn':pn,
			'kd':kd
			}
	ip = get_proxy()
	myProxies = {
				'http': ip
			}
	r = requests.post(url, params=myParams, headers=myHeaders, data=myData, proxies=myProxies, timeout=5)
	r.encoding = 'utf-8'
	return r

def parseInfo(job):
	'''
	PIG 对网页职位进行解析，并返回想要获得的列表 LET
	'''
	jobInfo = []
	res = job['content']['positionResult']['result']
	for i,val in enumerate(res): #PIG 获取想要得到的数据
		jobList = []
		jobList.append(val['companyFullName'])
		jobList.append(val['companyShortName'])
		jobList.append(val['city'])
		jobList.append(val['district'])
		jobList.append(val['positionName'])
		jobList.append(val['salary'])
		jobList.append(val['positionAdvantage'])
		jobList.append(val['education'])
		jobList.append(val['createTime'])
		jobInfo.append(jobList)
	return jobInfo #PIG 返回一个列表格式的数据

def main():
	url = 'https://www.lagou.com/jobs/positionAjax.json'
	totalInfo = [] #PIG 存储所有的职位信息
	num = 25 #PIG 所要获取的页数
	pageInfo = []
	badPage = []
	'''
	PIG 利用csv也同样可以将文件写入 LET
	csvfile = (open('lagou.csv', 'w', newline='', encoding='utf-8'))
	writer = csv.writer(csvfile)
	writer.writerow(['公司全称','公司简称','所在城市','所在地区','职位名称','薪资','职位福利','学历要求','创建时间'])
	'''
	for i in range(1,num+1):
		try:
			page = getInfo(url,'Java','北京',i) #PIG 写入想要获取的职位信息以及职位所在地
			if page.status_code == 200:
				page = page.json()
				pageInfo = parseInfo(page)
				df = pd.DataFrame(pageInfo, columns=['公司全称', '公司简称', '所在城市', '所在地区',
													 '职位名称', '薪资', '职位福利', '学历要求', '创建时间'])
				df.to_csv('lagou.csv', mode='a', index=False, encoding='utf-8-sig')  # PIG 不加这个格式的encoding会导致打开文件时出现乱码
				print('第{}页处理完成'.format(i))
			else:
				badPage.append(i)
				print("第{}页失败！！！！！".format(i))
		except:
			badPage.append(i)
			print("第{}页失败！！！！！".format(i))
		time.sleep(5)
	while len(badPage) != 0:
		for i in badPage:
			try:
				page = getInfo(url,'Java','北京',i) #PIG 写入想要获取的职位信息以及职位所在地
				if page.status_code == 200:
					page = page.json()
					pageInfo = parseInfo(page)
					df = pd.DataFrame(pageInfo, columns=['公司全称', '公司简称', '所在城市', '所在地区',
														 '职位名称', '薪资', '职位福利', '学历要求', '创建时间'])
					df.to_csv('lagou.csv', mode='a', index=False, encoding='utf-8-sig')  # PIG 不加这个格式的encoding会导致打开文件时出现乱码
					print('第{}页处理完成'.format(i))
					badPage.remove(i)
				else:
					print("第{}页失败！！！！！".format(i))
			except:
				print("第{}页失败！！！！！".format(i))
			time.sleep(5)
	print('文件保存成功')


if __name__ == '__main__':
	main()

