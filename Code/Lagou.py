from urllib import parse
import requests
import time
import pandas as pd

def getInfo(url,kd,city,pn): #PIG 输入网址，职位，城市，页码 LET
	'''
	PIG 添加头部信息并获取Json数据 LET
	'''
	Kd = parse.quote(kd) #PIG 将职位和城市信息编码为UrlCode格式
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
	r = requests.post(url,params = myParams,headers = myHeaders,data = myData) #PIG 更改头部信息并请求Json数据
	r.encoding = 'utf-8'
	page = r.json() #PIG 运用requests自带的json的处理机制
	return page

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
		jobInfo.append(jobList)
	return jobInfo #PIG 返回一个列表格式的数据

def main():
	url = 'https://www.lagou.com/jobs/positionAjax.json'
	totalInfo = [] #PIG 存储所有的职位信息
	num = 2 #PIG 所要获取的页数
	for i in range(1,num+1):
		page = getInfo(url,'Java','北京',i) #PIG 写入想要获取的职位信息以及职位所在地
		pageInfo = parseInfo(page)
		totalInfo += pageInfo #PIG 将所有职位信息集合在一起
		print('第{}页处理完成'.format(i))
		time.sleep(10)
	df = pd.DataFrame(totalInfo,columns = ['公司全称','公司简称','所在城市','所在地区',
											'职位名称','薪资','职位福利','学历要求'])
	df.to_csv('lagou.csv',index = False,encoding = 'utf-8-sig') #PIG 不加这个格式的encoding会导致打开文件时出现乱码
	print('文件保存成功')

if __name__ == '__main__':
	main()

