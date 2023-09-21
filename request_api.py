# import requests
# from pprint import pprint
#
# hello_response = requests.get("http://127.0.0.1:8000/random")
# video_response = requests.get("http://127.0.0.1:8000/video?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DbSvTVREwSNw")
#
# pprint(hello_response.json())
# pprint(video_response.json())
import requests

url = "https://telesign-telesign-send-sms-verification-code-v1.p.rapidapi.com/sms-verification-code"

querystring = {"phoneNumber":"7722087410","verifyCode":"0"}

headers = {
	"X-RapidAPI-Key": "37d1d817c6msh418838341e06d07p133704jsn25c68f19d1cb",
	"X-RapidAPI-Host": "telesign-telesign-send-sms-verification-code-v1.p.rapidapi.com"
}

response = requests.post(url, headers=headers, params=querystring)

print(response.json())