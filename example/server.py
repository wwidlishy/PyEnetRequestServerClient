from pyenet_sc import *
from request_parser import parse_request

def onConnect(event):
    print(f"Client connected from {event.peer.address}")
    r = Request("msg", {"text": "Hello, Client!"})
    server.send_data(event, r.serialize())
    
def onDisconnect(event):
    print(f"Client disconnected: {event.peer.address}")

def onRecv(event):
    data = server.recieve_data(event)
    if data:
        raw, address = data
        request = Request.deserialize(raw)
        parse_request(server, event, address, request)

server: Server = Server('localhost', 24337, onConnect, onDisconnect, onRecv)
server.mainloop()
