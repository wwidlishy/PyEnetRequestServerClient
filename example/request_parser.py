from pyenet_sc import *

def parse_request(self: object, event: object, address: object, r: Request) -> bool:
    if r.requestId == "msg":
        if "text" in r.requestData.keys():
            print(f"Message from {address}: '{r.requestData['text']}'")
            return True
    
    if r.requestId == "add":
        if "nums" in r.requestData.keys():
            if isinstance(r.requestData["nums"], list):
                result = 0
                for i in r.requestData["nums"]:
                    result += i

                r2: Request = Request("addResult", {"result": result})
                self.send_data(event, r2.serialize())

                print(f"Add from {address}: Performing addition on {r.requestData['nums']}, result={result}, Sending AddResult Request")
                return True
    if r.requestId == "addResult":
        if "result" in r.requestData.keys():
            print(f"AddResult from {address}: {r.requestData['result']}")
            return True
    return False