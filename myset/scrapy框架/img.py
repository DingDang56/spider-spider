from PIL import Image
import numpy as np
import requests as req
from io import BytesIO

def read_image(imageName):
    im = Image.open(imageName).convert('RGB')
    data = np.array(im)
    return data

def read_image_url(img_url):
    response = req.get('http://'+img_url)
    im = Image.open(BytesIO(response.content)).convert('RGB')
    data = np.array(im)
    return data

def get_num(n):
    l_num = []
    m = 0
    x = n
    while True:
        if m < 9:
            x0,x1, = np.split(x, [30],axis = 1)
            #print(x0)
            #plt.imshow(x0)
            #plt.pause(0.001)
            #print(x1)
            #plt.imshow(x1)
            #plt.pause(0.001)
            l_num.append(x0)
            x = x1
            m+=1
            continue
        else:
            l_num.append(x)
            #plt.imshow(x)
            #plt.pause(0.001)
            break
    return l_num

def get_0_9():
    l_num = get_num(read_image('3.png'))
    x2,x4,x3,x6,x8,x5,x1,x9,x0,x7 = l_num
    list_num = [x0,x1,x2,x3,x4,x5,x6,x7,x8,x9]
    return list_num

def get_num_list(png):
    l = []
    list_num = get_0_9()
    l_num_test = get_num(read_image_url(png))
    for i in range(0,10):
        #plt.imshow(l_num_test[i])
        #plt.pause(0.001)
        for w in range(0,10):
            #print((i == w).all())
            if (l_num_test[i] == list_num[w]):
                #plt.imshow(w)
                #plt.pause(0.001)
                l.append(w)
                #print(w)
                break
    #print (l)
    return l

a = get_num_list('static8.ziroom.com/phoenix/pc/images/price/e1b89727400c2b61fe1018661fada079s.png')
print(a)