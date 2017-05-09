# coding=utf-8
from framework.data_proc.jsonLib import get_pretty
from framework.http.httpLib import HttpLib
from framework.support.log import log_info


def search(search_string):
    url = "https://api.vk.com/method/places.search"
    params = {'latitude': 54.001343,
              'longitude': 27.669942,
              'radius': 2,
              'q': search_string,
              'access_token': '014d3430a604a0e5e4ebc684e011ad149c37280e6d34cbb1d6b19c59926b38629797283d0e63c77127235',
              'v': '5.64'}
    res = HttpLib(url=url,
                  params=params).send_get()
    for place in res.response.json()['response']['items']:
        print get_pretty(place)# log_info(get_pretty(res.response.json()['response']['items']))


search('Лесной')