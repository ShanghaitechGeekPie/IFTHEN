import pymongo

def connect_to_mongodb():
    connection = pymongo.MongoClient()
    db = connection['API']
    return db

class API():
    def __init__(self, _name, _type, _args, _return_type, _call_type, \
                 _request_url=None, _native_function=None, _id=None):
        self.name = _name
        self.type = _type
        self.args = _args
        self.return_type = _return_type
        self.call_type = _call_type
        self.request_url = _request_url
        self.native_function = _native_function
        self._id = _id

    @staticmethod
    def create(_name, _type, _args, _return_type, _call_type, \
               _request_url=None, _native_function=None, _id=None):
        return API(_name, _type, _args, _return_type, _call_type, _request_url, _native_function, _id)

    @staticmethod
    def get(_name):
        db = connect_to_mongodb()
        args = {
            'name': _name,
        }
        apis = db['API']
        api = apis.find_one(args)
        if api is None:
            return None
        return API(api['name'], api['type'], api['args'], api['return_type'], api['call_type'], \
                   api['request_url'], api['native_function'], api['_id'])

    def remove(self):
        db = connect_to_mongodb()
        apis = db['API']
        return apis.find_one_and_delete({'_id': self._id})

    def save(self):
        db = connect_to_mongodb()
        apis = db['API']
        if self._id is None:
            apis.insert({
                'name': self.name,
                'type': self.type,
                'args': self.args,
                'return_type': self.return_type,
                'call_type': self.call_type,
                'request_url': self.request_url,
                'native_function': self.native_function
            })
            return True
        else:
            apis.update({'_id': self._id}, {'$set': {
                'name': self.name,
                'type': self.type,
                'args': self.args,
                'return_type': self.return_type,
                'call_type': self.call_type,
                'request_url': self.request_url,
                'native_function': self.native_function
            }})
            return True
        return False


class Variable():
    def __init__(self, _key, _value, _id=None):
        self.key = _key
        self.value = _value
        self._id = _value

    @staticmethod
    def create(_key, _value, _id=None):
        return API(_key, _value, _id)

    @staticmethod
    def get(_key):
        db = connect_to_mongodb()
        args = {
            'key': _key,
        }
        _vars = db['Var']
        var = _vars.find_one(args)
        if var is None:
            return None
        return API(var['key'], var['value'], var['_id'])

    def remove(self):
        db = connect_to_mongodb()
        _vars = db['Var']
        return _vars.find_one_and_delete({'_id': self._id})

    def save(self):
        db = connect_to_mongodb()
        _vars = db['API']
        if self._id is None:
            _vars.insert({
                'key': self.key,
                'value': self.value
            })
            return True
        else:
            _vars.update({'_id': self._id}, {'$set': {
                'key': self.key,
                'value': self.value
            }})
            return True
        return False
