import pytest
import requests


class TestWeather:
    def test_weather(self):
        BaseUrl = "https://api.openweathermap.org/data/2.5/weather?"
        API = BaseUrl + "lat={lat}&lon={lon}&appid={appid}"
        url = API.format(lat="16.159185", lon="74.815620", appid="2f61c228521356a682a4e96e5f2429e6")
        re = requests.get(url)
        response = re.json()
        assert response['name'] == 'Gokak', "Expected to be Gokak but got " + response['name']

    def test_geocod(self):
        Baseurl = "http://api.openweathermap.org/geo/1.0/direct?"
        API = Baseurl + "q={city_name}&limit={limit}&appid={appid}"
        url = API.format(city_name="Gokak", limit=5, appid="2f61c228521356a682a4e96e5f2429e6")
        re = requests.get(url)
        response = re.json()
        assert response[0]['state'] == 'Karnataka', "Expected Karnataka but got" + response[0]["state"]
        assert response[0]['lat'] == 16.1693033, "Expected 16.159184 but got "+ str(response[0]['lat'])
