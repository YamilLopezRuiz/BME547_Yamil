import requests


r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/yl625")
print(r.status_code)
print(r.text)

r2 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F4")
print(r2.status_code)
print(r2.text)

r3 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M4")
print(r3.status_code)
print(r3.text)


if r3.text == r2.text:
    print("true")
else:
    print("false")

check_patient = {"Name": "yl625", "Match":  "No"}

r_check = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=check_patient)
print(r_check.text)
