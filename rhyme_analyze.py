import requests
import pytest
import json

QUERY_CODES = { "Means like" : "ml", "Sounds Like" : "sl",
                "Spelled like" : "sp", "Popular nouns" : "rel_jja",
               "Popular adjectives" : "rel_jjb", "Antonyms" : "rel_ant",
               "Hypernyms" : "rel_spc", "Hyponynms" : "rel_gen"
               "Comprises": "rel_com", "Part Of": "rel_par",
               "Frequent followers" : "rel_bga", "Perfect Rhymes" : "rel_rhy",
               "Approx. Rhymes" : "rel_nry", "Homophones" : "rel_hom",
               "Consonant Match" : "rel_cns"}
class DatamuseRequestObject():
    '''
    Stores response from Datamuse API
    '''
    response = []
    apihook = "https://api.datamuse.com/"
    status_code = None

    def __init__(self, query : str, search : str):
        #TODO: extend query string
        self.apicall = "/words?{}={}".format(query, search)

    def connect(self):
        r = requests.get(self.apihook + self.apicall)
        self.status_code = r.status_code
        self.response = r.json()

    def __bool__(self):
        return True if (self.status_code == 200 and self.response) else False


def get_rhyme(word : str, top=7):
    '''
    returns top n rhymes for a given word

    :param word: word to find rhymes for
    :param top: how many top words to return
    '''
    rhyme_request = DatamuseRequestObject("rel_rhy", word)
    rhyme_request.connect()
    return ", ".join([ jsonword.get("word") for jsonword in rhyme_request.response[0:top]]) if rhyme_request else "No Rhyme Found"


@pytest.fixture(scope='session')
def request_obj():
        request_obj = DatamuseRequestObject("sl", "biggie")
        return request_obj


def test_apicall(request_obj):
    assert request_obj.apicall == "/words?sl=biggie"


def test_connection(request_obj):
    request_obj.connect()
    assert request_obj.status_code == 200


def test_get_rhyme():
    assert get_rhyme("word", 3) == 'bluebird, bird, absurd'

def test_get_rhyme_false():
    assert get_rhyme("superfragilistictictactoe") == "No Rhyme Found"
