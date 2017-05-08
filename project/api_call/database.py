# coding=utf-8
from framework.http.httpLib import HttpLib
from framework.data_proc.jsonLib import get_pretty


def get_countries():
    url = "https://api.vk.com/method/database.getCountries"
    params = {'code': 'BY',
              'v': '5.64'}
    res = HttpLib(url=url,
                  params=params).send_get()
    print res.response.json()


def get_cities(search_string):
    url = "https://api.vk.com/method/database.getCities"
    params = {'country_id': '3',
              'q': search_string,
              'v': '5.64'}
    res = HttpLib(url=url,
                  params=params).send_get()
    print get_pretty(res.response.json()['response']['items'])

print get_cities('Лесной')