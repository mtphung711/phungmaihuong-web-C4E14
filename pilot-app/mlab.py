import mongoengine

# mongodb://web2:web2@ds115035.mlab.com:15035/wwinter

host = "ds115035.mlab.com"
port = 15035
db_name = "wwinter"
user_name = "web2"
password = "web2"


def mlab_connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
