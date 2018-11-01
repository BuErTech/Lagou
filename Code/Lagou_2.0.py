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
'''
PROXY_POOL_URL = 'http://localhost:5555/random'

def get_proxy():
	PIG 调用别人的代理池
		https://github.com/Python3WebSpider/ProxyPool
	LET
	try:
		response = requests.get(PROXY_POOL_URL)
		if response.status_code == 200:
			return response.text
	except ConnectionError:
		return None
'''

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
			'Cookie':'user_trace_token=20181011123107-316e80dd-e0df-437b-838f-3662f534f5f2; _ga=GA1.2.981321641.1539232336; '
					 'LGUID=20181011123217-a25cb1dd-cd0e-11e8-bbb2-5254005c3644; index_location_city=%E5%8C%97%E4%BA%AC; '
					 '_gid=GA1.2.1644222620.1540819087; JSESSIONID=ABAAABAABEEAAJAFD37850FD9F8513FCD8579981B7865DE; _gat=1;'
					 ' LGSID=20181030213710-e72b195a-dc48-11e8-b7bf-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; '
					 'PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1540276930,1540869433,1540903404,1540906633; '
					 'TG-TRACK-CODE=index_navigation; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1540906650;'
					 ' LGRID=20181030213727-f14a299f-dc48-11e8-b7bf-525400f775ce; SEARCH_ID=028a5fb86c2a438895d00b02b9273b4b',
			'User-Agent':random.choice(USER_AGENTS),
			'Referer':'https://www.lagou.com/jobs/list_'+Kd+'?px=default&city='+City
			}
	myData = {
			'first':'true',
			'pn':pn,
			'kd':kd
			}
	#ip = get_proxy()
	r = requests.post(url, params=myParams, headers=myHeaders, data=myData,  timeout=5)#proxies=myProxies,
	r.encoding = 'utf-8'
	#page = r.json()
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
		jobList.append(val['positionId'])
		jobInfo.append(jobList)
	return jobInfo #PIG 返回一个列表格式的数据

def main():
	url = 'https://www.lagou.com/jobs/positionAjax.json'
	totalInfo = [] #PIG 存储所有的职位信息
	num = 10 #PIG 所要获取的页数
	pageInfo = []
	pages = []
	'''
	PIG 利用csv也同样可以将文件写入 LET
	csvfile = (open('lagou.csv', 'w', newline='', encoding='utf-8'))
	writer = csv.writer(csvfile)
	writer.writerow(['公司全称','公司简称','所在城市','所在地区','职位名称','薪资','职位福利','学历要求','创建时间', '职位ID'])
	'''
	for i in range(1, num+1):
		pages.append(i)
	pages.reverse() #PIG 因为要倒序输出，所以先倒置列表
	while True:
		for i in range(len(pages)-1, -1, -1):
			try:
				page = getInfo(url,'Java','北京',pages[i]) #PIG 写入想要获取的职位信息以及职位所在地
				if page.status_code == 200:
					page = page.json()
					pageInfo = parseInfo(page)
					df = pd.DataFrame(pageInfo, columns=['公司全称', '公司简称', '所在城市', '所在地区',
														 '职位名称', '薪资', '职位福利', '学历要求', '创建时间', '职位ID'])
					df.to_csv('lagou.csv', mode='a', index=False, encoding='utf-8-sig')  # PIG 不加这个格式的encoding会导致打开文件时出现乱码
					print('第{}页处理完成'.format(pages[i]))
					del(pages[i])
				else:
					print("第{}页失败！！！！！".format(pages[i]))
			except:
				print("第{}页失败！！！！！".format(pages[i]))
			time.sleep(3)
		if len(pages) == 0:
			break
	print('文件保存成功')


if __name__ == '__main__':
	main()

