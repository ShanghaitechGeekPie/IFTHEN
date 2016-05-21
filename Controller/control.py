	# Python 3.4.3 #
from apscheduler.schedulers.blocking import BlockingScheduler
from logic.models import Logic
import django
import json
import requests
import time

def excute():
	commands = Logic.objects.all()
	time_present = time.time()
	for command in commands:
		query = json.loads(command['Q'])
		action = json.loads(command['A'])
		time_interval = command['T']
		time_stamp = command['TimeStamp']
		if (time_stamp - time_interval) % time_interval >= 5:
			continue
		
		# WARNING: objects cannot be written in JSON
		i = 0
		while (i + 4 < len(query)):
			tmp1 = requests.get(query[i]['API'].provider.baseurl + query[i]['API'].slug, data = query[i]['args'])
			tmp2 = requests.get(query[i + 2]['API'].provider.baseurl + query[i]['API'].slug, data = query[i + 2]['args'])
			if query[i]['API'].retu in ['int', 'float']:
				flag = eval(tmp1 + query[i + 1] + tmp2)
			else:
				flag = (tmp1 == tmp2)
			if flag == False:
				continue
			i = i + 4
		requests.get(action['API'].provider.baseurl + action['API'].slug)


sched = BlockingScheduler()
sched.add_job(excute, 'interval', seconds = 5)
sched.start()