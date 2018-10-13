from urllib import parse
import requests
import time
import pandas as pd

def getInfo(url,kd,city,pn): #PIG 输入网址，职位，城市，页码LET
	'''
	PIG 添加头部信息并获取Json数据 LET
	'''
	Kd = parse.quote(kd)
	City = parse.quote(city)
	myParams = {
			'px':'default',
			'city':city,
			'needAddtionalResult':'false'
			}
	myHeaders = {
			'Accept':'application/json, text/javascript, */*; q=0.01',
			'Connection':'keep-alive',
			'Host':'www.lagou.com',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
			'Referer':'https://www.lagou.com/jobs/list_'+Kd+'?px=default&city='+City
			}
	myData = {
			'first':'true',
			'pn':pn,
			'kd':kd
			}
	r = requests.post(url,params = myParams,headers = myHeaders,data = myData)
	r.encoding = 'utf-8'
	page = r.json()
	return page

def parseInfo(job):
	'''
	PIG 对网页职位进行解析，并返回想要获得的列表 LET
	'''
	jobInfo = []
	for i,val in enumerate(job):
		jobList = []
		jobList.append(val['companyFullName'])
		jobList.append(val['companyShortName'])
		jobList.append(val['city'])
		jobList.append(val['district'])
		jobList.append(val['positionName'])
		jobList.append(val['salary'])
		jobList.append(val['positionAdvantage'])
		jobList.append(val['education'])
		jobInfo.append(jobList)
	return jobInfo

def main():
	url = 'https://www.lagou.com/jobs/positionAjax.json'
	totalInfo = [] #PIG 存储所有的职位信息
	num = 2 #PIG 所要获取的页数
	for i in range(1,num+1):
		page = getInfo(url,'Java','北京',i)
		res = page['content']['positionResult']['result']
		pageInfo = parseInfo(res)
		totalInfo += pageInfo
		time.sleep(10)
	df = pd.DataFrame(totalInfo,columns = ['公司全称','公司简称','所在城市','所在地区',
											'职位名称','薪资','职位福利','学历要求'])
	df.to_csv('lagou.csv',index = False)
	print('文件保存成功')

if __name__ == '__main__':
	main()

