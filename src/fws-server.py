from flask import Flask
from flask_websockets import WebSockets

app = Flask(__name__)
sockets = WebSockets(app)

@sockets.on_message
def echo(message):
    return message

ipaddr = 'localhost'
PORT = 5500

if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer((ipaddr, PORT), app, handler_class=WebSocketHandler)
    server.serve_forever()