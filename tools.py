import re
import base64
from PIL import Image
import numpy as np
import pickle

def save_img(url):
    imgstr = re.search(r'base64,(.*)', url).group(1)
    output = open('static/user_img.jpg', 'wb')
    output.write(base64.b64decode(imgstr))
    output.close()

def img_to_arr():
    im = Image.open('static/user_img.jpg')
    im = im.resize((28,28), resample=Image.BICUBIC)
    arr = np.array(im)[:,:,0]
    return arr

def load_model():
    model = pickle.load(open('static/trained_digits.sav', 'rb'))
    return model