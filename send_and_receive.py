import requests


out_data = {"user": "rr238", "message": "try again"}


r_post = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                       json=out_data)
print(r_post.status_code)
print(r_post.text)


r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/yl625")
print(r.status_code)
print(r.text)
