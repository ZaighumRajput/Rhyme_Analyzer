import requests
import pytest


class datamuse_request_object():
    response = []
    apihook = "https://api.datamuse.com/"
    status_code = "not connected"

    def __init__(self, query : str, search : str, code=None):
        self.apicall = "/words?{}={}".format(query, search)

    def connect(self):
        r = requests.get(self.apihook + self.apicall)
        self.status_code = r.status_code



class Test_Datamust_request_object:

    def test_apicall_string(cls):
        first = datamuse_request_object("sl", "biggie")
        assert first.apicall ==  "/words?sl=biggie"

    def test_connection(cls):
        first = datamuse_request_object("sl", "biggie")
        first.connect()
        assert first.status_code == 200

    def test_response(cls):
        first = datamuse_request_object("sl", "biggie")

