import tornado.web
import tornado.httpclient
import json
import models
import datetime
import requests


class DefaultHandler(tornado.web.RequestHandler):
    def get(self):
        msg = {'message': 'Welcome to IFTHEN API server.', 'status': True}
        self.write(json.dumps(msg))


class AllAPIHandler(tornado.web.RequestHandler):
    pass

class QueryHandler(tornado.web.RequestHandler):
    def get(self, api_name):
        api = models.API.get(_name=api_name)
        if api is None:
            self.write(json.dumps({
                'message': 'No such API: ' + api_name,
                'status': False
            }))
            return
        if api.call_type == 'http':
            params = {}
            for a in api.args:
                params[a['key']] = self.get_argument(a['key'])
            response = requests.get(api.request_url, params=params)
            self.write(json.dumps({
                'value': eval(api.native_function),
                'status': True
            }))
            #self.write(response.text)
        elif api.call_type == 'native':
            self.write(json.dumps({
                'value': eval(api.native_function),
                'status': True
            }))
        return


class ActionHandler(tornado.web.RequestHandler):
    def post(self):
        pass
