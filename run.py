import numpy as np
from kNN import KNN


X = np.array([
  [39, 27, 6],
  [48, 17, 6],
  [18, 22, 6],
  [39, 34, 7],
  [62, 118, 7],
  [59, 137, 7],
  [95, 131, 2],
  [86, 110, 3],
  [185, 155, 3],
  [193, 129, 4],
  [164, 135, 5],
  [205, 131, 5],
  [125, 55, 5],
  [168, 35, 9],
  [135, 47, 9],
  [149, 66, 9]]).astype(np.float64)


height = int(input('Введите рост особи: '))
weight = int(input('Введите вес особи: '))

obj = np.array([height, weight]).astype(np.float64)


k = 3
cl = KNN()
cl.fit(X[:, 0:-1], X[:, -1])
object_class = cl.predict(obj, k)


monkeys = {1: 'lemur', 2: 'schimpanze', 3: 'gorilla', 4: 'orangutan'}
print('/nРезультат классификации: ', monkeys[object_class])