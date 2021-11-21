import requests
from django.conf import settings


def sms(phone, data):
    print(phone, data)
    query = {'key': settings.SMS_API_KEY,
             'password': settings.SMS_API_PWD,
             'from': settings.SMS_API_FROM,
             'to': str(phone), 'msg': data['title'] + " " + data["description"]}
    response = requests.get('https://api2.smsplanet.pl/sms', params=query)
    print(response.json())
