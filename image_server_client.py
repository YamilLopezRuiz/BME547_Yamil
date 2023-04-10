from tkinter import filedialog
import base64
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
from skimage.io import imsave
from flask import Flask, request, jsonify
import logging
import requests

server = "http://vcm-21170.vm.duke.edu"

app = Flask(__name__)


# Select image to upload
def select_image():
    filename = filedialog.askopenfilename()
    return filename


# Convert image to base64 string
def convert_image_file_to_base64_string(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


# Download watermarked image
def convert_base64_string_to_image_file(b64_string):
    image_bytes = base64.b64decode(b64_string)
    with open("new_messi.jpg", "wb") as out_file:
        out_file.write(image_bytes)
    return


def main():
    filename = select_image()
    if filename == "":
        return
    b64_image = convert_image_file_to_base64_string(filename)
    # print(b64_image)
    id = 5
    net_id = "yl625"
    image_dict = {"image": b64_image, "net_id": net_id, "id_no": id}
    r = requests.post(server + "/add_image", json=image_dict)
    print(r.status_code)
    print(r.text)
    r = requests.get(server + "/get_image/yl625/5")
    print(r.status_code)
    # print(r.text)
    convert_base64_string_to_image_file(r.text)


if __name__ == "__main__":
    main()
