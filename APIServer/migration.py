from models import API

# 1. The time api
try:
    API.get(_slug='time').remove()
except:
    pass
API.create(
    _name='当前时间',
    _slug='time',
    _type='query',
    _args=[],
    _return_type='int',
    _call_type='native',
    _request_url='',
    _native_function='datetime.datetime.now().timestamp()',
    _authority=''
).save()

# 2. The weather api
try:
    API.get(_slug='weather').remove()
except:
    pass
API.create(
    _name='当前天气',
    _slug='weather',
    _type='query',
    _args=[
        {'key': 'location', 'name': 'City Name', 'type': 'string', 'placeholder': '城市名', 're': ''}
    ],
    _return_type='string',
    _call_type='http',
    _request_url='http://api.thinkpage.cn/v3/weather/now.json?key=t1x7hnxlkb0kyvl8&language=en&unit=c',
    _native_function='json.loads(response.text)[\'results\'][0][\'now\'][\'text\']',
    _authority=''
).save()

# 3. The get api
try:
    API.get(_slug='get').remove()
except:
    pass
API.create(
    _name='取变量',
    _slug='get',
    _type='query',
    _args=[
        {'key': 'key', 'name': 'Key', 'type': 'string', 'placeholder': '变量名', 're': ''}
    ],
    _return_type='',
    _call_type='native',
    _request_url='',
    _native_function='models.Variable.get(params[\'key\']).value',
    _authority=''
).save()

# 4. The set api
try:
    API.get(_slug='set').remove()
except:
    pass
API.create(
    _name='存变量',
    _slug='set',
    _type='action',
    _args=[
        {'key': 'key', 'name': 'Key', 'type': 'string', 'placeholder': '变量名', 're': ''},
        {'key': 'value', 'name': 'Value', 'type': '', 'placeholder': '值', 're': ''}
    ],
    _return_type='',
    _call_type='native',
    _request_url='',
    _native_function='models.Variable.set(params[\'key\'], params[\'value\'])',
    _authority=''
).save()

# 5. The mail send api
try:
    API.get(_slug='sendmail').remove()
except:
    pass
API.create(
    _name='发送邮件',
    _slug='sendmail',
    _type='action',
    _args=[
        {'key': 'to', 'name': 'Receiver', 'type': 'string', 'placeholder': '收件地址', 're': ''},
        {'key': 'msg', 'name': 'Message', 'type': 'string', 'placeholder': '邮件内容', 're': ''}
    ],
    _return_type='',
    _call_type='native',
    _request_url='',
    _native_function='utils.sendmail(params[\'to\'], params[\'msg\'])',
    _authority=''
).save()

# 6. The echo api
try:
    API.get(_slug='echo').remove()
except:
    pass
API.create(
    _name='回声',
    _slug='echo',
    _type='query',
    _args=[
        {'key': 'value', 'name':'Content', 'type': 'string', 'placeholder': '任意内容', 're': ''}
    ],
    _return_type='',
    _call_type='native',
    _request_url='',
    _native_function='self.get_argument(params[\'value\'])',
    _authority=''
).save()
