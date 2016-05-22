import tornado.web
import tornado.httpclient
import json
import models
import datetime
import requests

import utils

class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.set_header("Access-Control-Allow-Origin", "*")

class DefaultHandler(BaseHandler):
    def get(self):
        msg = {'message': 'Welcome to IFTHEN API server.', 'status': True}
        self.write(json.dumps(msg))


class AllAPIHandler(BaseHandler):
    def get(self):
        apis = models.API.get_all()
        ret = {'name':'Basic', 'apis': []}
        for a in apis:
            ret['apis'].append({
                'name': a.name,
                'slug': a.slug,
                'type': a.type,
                'args': a.args,
                'retu': a.return_type,
                'authority': a.authority
            })
        self.finish(json.dumps(ret))


class APIHandler(BaseHandler):
    def get(self, api_name):
        api = models.API.get(_slug=api_name)
        if api is None:
            self.write(json.dumps({
                'message': 'No such API: ' + api_name
            }))
            return
        if api.call_type == 'http':
            params = {}
            for a in api.args:
                params[a['key']] = self.get_argument(a['key'])
            response = requests.get(api.request_url, params=params)
            self.write(json.dumps({
                'result': eval(api.native_function)
            }))
        elif api.call_type == 'native':
            params = {}
            for a in api.args:
                params[a['key']] = self.get_argument(a['key'])
            self.write(json.dumps({
                'result': eval(api.native_function)
            }))
        return


# class ActionHandler(tornado.web.RequestHandler):
#     def post(self):
#         pass
