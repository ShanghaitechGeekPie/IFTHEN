# -*- coding: utf-8 -*-
# @Author: eastpiger
# @Date:   2016-05-22 03:55:18
# @Last Modified by:   eastpiger
# @Last Modified time: 2016-05-22 09:45:15
import requests, json
from django.http import HttpResponse, JsonResponse

from IFTHEN_db.models import Provider, API, Logic

def get_apis(request):
	providers = Provider.objects.all()
	response_data = [{
		'id': provider.id,
		'name': provider.name,
		'baseurl': provider.baseurl,
		'APIs': [
			{
				'provider': {
					'id': provider.id,
					'name': provider.name,
					'baseurl': provider.baseurl,
				},
				'id': API.id,
				'name': API.name,
				'slug': API.slug,
				'type': API.type,
				'args': API.args,
				'return': API.retu,
				'authority': API.authority,
			} for API in provider.api_set.all()
		]
	} for provider in providers]

	return JsonResponse(response_data, safe=False)

def import_provider(request):
	base_url = request.GET['baseurl']

	APIList = json.loads(requests.get(base_url + 'APIList').text)

	tProvider = Provider(
		name= APIList['name'],
		baseurl= base_url,
	)
	tProvider.save()

	for i in APIList['apis']:
		tAPI = API(
			provider= tProvider,
			name= i['name'],
			slug= i['slug'],
			type= i['type'],
			args= json.dumps(i['args']),
			retu= json.dumps(i['retu']),
			authority= i['authority'],
		)
		tAPI.save()

	response_data = {'result': 'success'}
	return JsonResponse(response_data, safe=False)

def _JsonToQ(Q):
	Q = json.loads(Q)
	response_data = []

	for i in Q:
		if i in ('and', 'or', 'not'):
			response_data.append(i)
		elif i in ('=', '!=', '<', '>', '<=', '>='):
			response_data.append(i)
		else:
			t = API.objects.get(id = i['API'])
			response_data.append({
				'provider': {
					'id': t.provider.id,
					'name': t.provider.name,
					'baseurl': t.provider.baseurl,
				},
				'id': t.id,
				'name': t.name,
				'slug': t.slug,
				'type': t.type,
				'args': t.args,
				'return': t.retu,
				'authority': t.authority,
				'argus': i['args'],
			})

	return response_data

def _JsonToA(A):
	A = json.loads(A)
	response_data = []

	for i in A:
		t = API.objects.get(id = i['API'])
		response_data.append({
			'provider': {
				'id': t.provider.id,
				'name': t.provider.name,
				'baseurl': t.provider.baseurl,
			},
			'id': t.id,
			'name': t.name,
			'slug': t.slug,
			'type': t.type,
			'args': t.args,
			'return': t.retu,
			'authority': t.authority,
			'argus': i['args'],
		})

	return response_data

def get_logics(request):
	logics = Logic.objects.all()
	response_data = [{
		'id': logic.id,
		'name': logic.name,
		'describe': logic.describe,
		'Q': _JsonToQ(logic.Q),
		'A': _JsonToA(logic.A),
		'T': logic.T,
		'TimeStamp': logic.TimeStamp,
	} for logic in logics]

	return JsonResponse(response_data, safe=False)

def change_logic(request):
	changeform = json.loads(request.GET['form'])

	if changeform['command'] == "DELETE":
		logic = Logic.objects.get(id = changeform['id'])
		logic.delete()
	elif changeform['command'] == "UPDATE":
		logic = Logic.objects.get(id = changeform['id'])
		logic.name = changeform['name']
		logic.describe = changeform['describe'][:200]
		logic.Q = json.dumps(changeform['Q'])
		logic.A = json.dumps(changeform['A'])
		logic.T = changeform['T']
		logic.update()
	elif changeform['command'] == "INSERT":
		logic = Logic(
			name= changeform['name'],
			describe= changeform['describe'][:200],
			Q= json.dumps(changeform['Q']),
			A= json.dumps(changeform['A']),
			T= changeform['T'],
		)
		logic.save()

	response_data = {'result': 'success'}
	return JsonResponse(response_data, safe=False)
