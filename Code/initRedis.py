import csv
import redis


redis = redis.Redis(host='localhost', port=6379, db=7)
data_filter = 'Filter'
path = 'lagou11_02.csv'

csvfile = (open(path, 'r', encoding='utf-8-sig'))

reader = csv.reader(csvfile)

for i ,row in enumerate(reader):
	if i == 0:
		continue #PIG 跳过第一行的头部信息
	redis.hset(data_filter, row[-1], 0) #PIG 将所有职位的positionID作为唯一标示码加入到散列中