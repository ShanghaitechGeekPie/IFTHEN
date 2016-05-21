from controller import *
import tornado.ioloop
import tornado.httpserver

from tornado.options import define, options
define('port', default=8000, help="run on the given port", type=int)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'^/?$', DefaultHandler),
            (r'^/all/?$', AllAPIHandler),
            (r'^/api/([a-zA-Z0-9]+)/?$', QueryHandler)
        ],
        debug=True,
        autoreload=True,
    )
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port, address='0.0.0.0')
    tornado.ioloop.IOLoop.instance().start()
