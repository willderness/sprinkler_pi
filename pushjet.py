import requests

def register_service(name, icon):
    service = { "name": name, "icon": icon }
    resp = requests.post('https://api.pushjet.io/service', data=service).json()
    print(resp)
    return resp['service']

def push_msg(service_secret, msg):

    data = {
      'message': str(msg),
      'level': 5, 
      'secret': service_secret,
    }

    resp = requests.post('https://api.pushjet.io/message', data=data).json()
    print(resp)


#service_public = "98ea-852f0b-fae6206b53db-76fbe-43d1a982c"
#service_secret = "a65e46e7af577920572503dbcd332c43"

#service_resp = register_service("Sprinkler", "http://digibyte.com/waterdrop.png")
#service_secret = service_resp['secret']
#service_public = service_resp['public']
#print("Public: " + service_public)
#push_msg(service_secret, "Service Booted")


