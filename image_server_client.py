from tkinter import filedialog
import base64
# import matplotlib.image as mpimg
# from matplotlib import pyplot as plt
# from skimage.io import imsave

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

# Upload base64 string to server


# Download watermarked image
def convert_base64_string_to_image_file(b64_string):
    image_bytes = base64.b64decode(b64_string)
    image_buf = io.BytesIO(image_bytes)
    img_ndarray = mpimg.imread(image_buf, format='JPG')

def main():
    filename = select_image()
    if filename == "":
        return
    b64_image = convert_image_file_to_base64_string(filename)
    print(b64_image)

if __name__ == "__main__":
    main()