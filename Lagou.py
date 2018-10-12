from urllib import parse
import requests

def getJson(url,kd,city,pn): #PIG 输入网址，职位，城市，页码LET
	```
	PIG 获取JSON数据并加上头部信息 LET
	```
	Kd = parse.quote(kd)
	City = parse.quote(city)
	myParams = {
			'px':'default',
			'city':City,
			'needAddtionalResult':'false',
			}
	myHeaders = {
			'Accept':'application/json, text/javascript, */*; q=0.01',
			'Connection':'keep-alive',
			'Host':'www.lagou.com',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
			'Referer':'https://www.lagou.com/jobs/list_'+Kd+'?px=default&city=]'+City,
			}
	myData = {
			'first':'true',
			'pn':pn,
			'kd':kd,
			}
	r = requests.post(url,params = myParams,headers = myHeaders,data = myData)
	r.encoding = r.apparent.encoding
	page = r.json()
	return page



