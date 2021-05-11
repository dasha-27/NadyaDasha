from PIL import Image
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

bit_str = input("Количество бит для кодирования от 3 до 7: ")
bits = int(bit_str)

im = Image.open('image.jpg')
data = np.array(im.getdata()).reshape([im.height, im.width, 3])

x = np.arange(0, im.width)
X = np.array([x, x**2.0, x**3.0, x**4.0, x**5.0]).transpose()

plt.title('Цветовые каналы первой строки изображения')
plt.plot(data[0, :, 0], 'r-')
plt.plot(data[0, :, 1], 'g-')
plt.plot(data[0, :, 2], 'b-')
plt.grid()
plt.show()

y = data[0, :, 2]
lm = linear_model.LinearRegression()
lm.fit(X, y)
predicted = lm.predict(X)
plt.title('Описание строки изображения с помощью полинома 5 степени')
plt.plot(predicted, 'b--')
plt.plot(y, 'b-')
plt.grid()
plt.show()

bits_per_channel = bits
threshold = 2**(bits_per_channel-1)-1
red = 0
green = 1
blue = 2

pix_new = [[0]*3 for o in range(im.height)]

for w in range(im.height):
    for e in range(3):
        y = data[w, :, e]
        lm = linear_model.LinearRegression()
        lm.fit(X, y)
        predicted = lm.predict(X)
        diff = y - predicted
        diff = np.clip(diff, -threshold, threshold)
        y = predicted + diff
        y = np.clip(y, 0, 255)
        pix_new[w][e] = y.astype(int)

pix = im.load()
i = 0
j = 0
for i in range(im.height):
    for j in range(im.width):
        l = list(pix[j, i])
        l[red] = pix_new[i][red][j]
        l[green] = pix_new[i][green][j]
        l[blue] = pix_new[i][blue][j]
        pix[j, i] = tuple(l)

image = 'ready_' + bit_str + '_bits.png'
im.save(image)
