import requests


r = requests.get("https://api.github.com/repos/yl625/BME547_Yamil/branches")
print(r)
print(type(r))
print(r.status_code)
print(r.text)
branches = r.json()
print(branches)
for branch in branches:
    print(branch["name"])
