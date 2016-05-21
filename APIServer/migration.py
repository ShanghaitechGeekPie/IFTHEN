from models import API

# 1. The time api
API.get(_name='time').remove()
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
API.get(_name='weather').remove()
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
