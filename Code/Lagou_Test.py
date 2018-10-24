def getIps():
	ippool = []
	reader = csv.reader(open('ips.csv'))
	for row in reader:
		ippool.append([row[0], row[1]])
	return ippool
