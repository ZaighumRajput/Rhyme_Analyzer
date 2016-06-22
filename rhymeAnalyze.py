import requests



class datamuse_request_object():

    def __init__(self, query : str, search : str, code=None):
        self.apicall = "/words?{}={}".format(query, search)

def datamuse_api(search : str):
    Api_Url = "https://api.datamuse.com/"
    r = requests.get(url)
    return r.status_code

#def test_api_connection():
    #assert datamuse_api(search="biggie") == 200

def test_request_object_querystring():
    first = datamuse_request_object("sl", "biggie")
    first.apicall = "/words?sl=biggie"
