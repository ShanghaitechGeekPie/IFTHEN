# Python 3.4.3 #
from apscheduler.schedulers.blocking import BlockingScheduler
from logic.models import Logic
import django
import json
import requests
import time

def excute():
	commands = Logic.objects.all()
	for command in commands:
		time_present = time.time()
		query = json.loads(command['Q'])
		action = json.loads(command['A'])
		time_interval = command['T']
		time_stamp = command['TimeStamp']
		if (time_present - time_stamp) % time_interval >= 5:
			continue
		i = 0
		while (i + 4 < len(query)):
			API1 = API.objects.get(id = query[i]['API'])
			API2 = API.objects.get(id = query[i + 2]['API'])
			tmp1 = requests.get(API1.provider.baseurl + API1.slug, data = query[i]['args'])
			tmp2 = requests.get(API2.provider.baseurl + API2.slug, data = query[i + 2]['args'])
			if API1.retu in ['int', 'float']:
				flag = eval(tmp1 + query[i + 1] + tmp2)
			else:
				if qurey[i+1] == '=':
					flag = (tmp1 == tmp2)
				else:
					flag = (tmp1 != tmp2)
			if flag == False:
				continue
			i = i + 4
		API1 = API.objects.get(id = action['API'])
		requests.get(API1.provider.baseurl + API1.slug)

sched = BlockingScheduler()
sched.add_job(excute, 'interval', seconds = 5)
sched.start()