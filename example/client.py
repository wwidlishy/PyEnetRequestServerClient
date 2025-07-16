from pyenet_sc import *
from request_parser import parse_request

client: Client = InternetHandler.setup_client('127.0.0.1', 24337)

def onSelfConnect(event):
    r = Request("msg", {"text": "Hello Server!"})
    client.send_data(event, r.serialize())

    r = Request("add", {"nums": [1, 2, 3]})
    client.send_data(event, r.serialize())
    
def onEach(event):
    data = client.recieve_data(event)
    if data:
        raw, address = data
        request = Request.deserialize(raw)
        parse_request(client, event, address, request)

while True:
    client.update(onSelfConnect, onEach)