import requests
import pytest
import json

class DatamuseRequestObject():
    response = []
    apihook = "https://api.datamuse.com/"
    status_code = "not connected"

    def __init__(self, query : str, search : str):
        #TODO: extend query string
        self.apicall = "/words?{}={}".format(query, search)

    def connect(self):
        r = requests.get(self.apihook + self.apicall)
        self.status_code = r.status_code
        self.response = r.json()


def get_rhyme(word : str, top=7):
    rhyme_request = DatamuseRequestObject("rel_rhy", word)
    rhyme_request.connect()
    return ", ".join([ jsonword.get("word") for jsonword in rhyme_request.response[0:top]])

@pytest.fixture(scope='session')
def request_obj():
        request_obj = DatamuseRequestObject("sl", "biggie")
        return request_obj

def test_apicall(request_obj):
    assert request_obj.apicall == "/words?sl=biggie"

def test_connection(request_obj):
    request_obj.connect()
    assert request_obj.status_code == 200

def test_response(request_obj):
    assert request_obj.response == None


def test_get_rhyme():
    assert get_rhyme("word") == 'bluebird, bird, absurd, incurred, nerd, deterred, herd'