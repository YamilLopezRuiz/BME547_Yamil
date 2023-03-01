import requests


out_data = {"name": "Yamil Lopez-Ruiz", "net_id": "yl625",
            "e-mail": "yl625@duke.edu"}

r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
print(r.status_code)
print(r.text)
