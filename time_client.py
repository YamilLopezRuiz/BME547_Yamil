import datetime
import requests

#current_date = datetime.datetime.now()
#print(current_date)
#s1 = current_date.strftime("%m-%d-%Y")
#print(s1)
#s2 = current_date.strftime("%H:%M:%S")
#print(s2)

server = "http://127.0.0.1:5000"

r = requests.get(server + "/time")
print(r.status_code)
print(r.text)

r = requests.get(server + "/date")
print(r.status_code)
print(r.text)
