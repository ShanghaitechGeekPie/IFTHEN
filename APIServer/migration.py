from models import API

# 1. The time api
try:
    API.get(_name='time').remove()
except:
    pass
API.create(
    _name='time',
    _type='query',
    _args=[],
    _return_type='int',
    _call_type='native',
    _request_url=None,
    _native_function='datetime.datetime.now().timestamp()'
).save()

# 2. The weather api
try:
    API.get(_name='weather').remove()
except:
    pass
API.create(
    _name='weather',
    _type='query',
    _args=[
        {'key': 'location', 'name': 'City Name', 'type': 'string', 'placeholder': '城市名'}
    ],
    _return_type='string',
    _call_type='http',
    _request_url='http://api.thinkpage.cn/v3/weather/now.json?key=t1x7hnxlkb0kyvl8&language=en&unit=c',
    _native_function='json.loads(response.text)[\'results\'][0][\'now\'][\'text\']'
).save()

# 3. The get api
try:
    API.get(_name='get').remove()
except:
    pass
API.create(
    _name='get',
    _type='query',
    _args=[
        {'key': 'key', 'name': 'Key', 'type': 'string', 'placeholder': '变量名'}
    ],
    _return_type=None,
    _call_type='native',
    _request_url=None,
    _native_function='models.Variable.get(params[\'key\']).value'
).save()

# 4. The set api
try:
    API.get(_name='set').remove()
except:
    pass
API.create(
    _name='set',
    _type='action',
    _args=[
        {'key': 'key', 'name': 'Key', 'type': 'string', 'placeholder': '变量名'},
        {'key': 'value', 'name': 'Value', 'type': None, 'placeholder': '值'}
    ],
    _return_type=None,
    _call_type='native',
    _request_url=None,
    _native_function='models.Variable.set(params[\'key\'], params[\'value\'])'
).save()
