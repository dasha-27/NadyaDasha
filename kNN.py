import numpy as np
from sklearn.preprocessing import normalize

def k_nearest(X, k, obj):
    X_sub = X[:, 0:-1]
    X_sub = np.vstack((X_sub, obj))
    X_sub = normalize(X_sub, axis=0, norm='max')
    obj = X_sub[-1]
    X_sub = X_sub[:16, :2]

    a = [dist(i, obj) for i in X_sub]
    b = np.argsort(a)
    b = b[0:k]
    sub_X = X[[b], -1]

    unique, counts = np.unique(sub_X, return_counts=True)
    return unique[np.argmax(counts)]

def dist(A, B):
  try:
   r = 0
   for i in range(len(A)):
    r += (float(A[i]) - float(B[i]))*(float(A[i]) - float(B[i]))
    return np.sqrt(r)
  except Exception as e:
      print("Ошибка вычисления расстояния!")

