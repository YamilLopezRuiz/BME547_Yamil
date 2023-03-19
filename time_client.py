import requests

server = "http://127.0.0.1:5000"

r = requests.get(server + "/time")
print(r.status_code)
print(r.text)

r = requests.get(server + "/date")
print(r.status_code)
print(r.text)

age = {'date': "10-10-1999", 'units': "years"}
r = requests.post(server + "/age", json=age)
print(r.status_code)
print(r)
print(r.json())

r = requests.get(server + "/until_next_meal/breakfast")
print(r.status_code)
print(r.json())
