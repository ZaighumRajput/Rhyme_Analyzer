import requests
import pytest


class datamuse_request_object():
    response = []
    apihook = "https://api.datamuse.com/"
    status_code = "not connected"

    def __init__(self, query : str, search : str, code=None):
        #TODO: accomodate all options
        self.apicall = "/words?{}={}".format(query, search)

    def connect(self):
        r = requests.get(self.apihook + self.apicall)
        self.status_code = r.status_code
        self.response = r.json()


@pytest.fixture(scope='session')
def request_obj():
    request_obj = datamuse_request_object("sl", "biggie")
    return request_obj

def test_apicall(request_obj):
    assert request_obj.apicall == "/words?sl=biggie"

def test_connection(request_obj):
    request_obj.connect()
    assert request_obj.status_code == 200

def test_response(request_obj):
    assert request_obj.response == None
