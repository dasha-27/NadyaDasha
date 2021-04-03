import numpy as np
import random

#евклидово расстояние между двумя точками
def dist(A, B):
    try:
        r = 0
        if len(A) != len(B):
            return 0
        for i in range(len(A)):
            r += (A[i] - B[i])*(A[i] - B[i])
        return np.sqrt(r)
    except Exception:
        return 0

#возвращает список индексов ближайших центров по каждой точке
def class_of_each_point(X, centers):
    m = len(X)
    k = len(centers)

  #матрица расстояний от каждой точки до каждого центра
    distances = np.zeros((m, k))
    for i in range(m):
        for j in range(k):
            distances[i, j] = dist(centers[j], X[i])

  #поиск ближайшего центра для каждой точки
    return np.argmin(distances, axis=1)


def kmeans(k, X):
    m = X.shape[0]
    n = X.shape[1]
    print("m = ", m, "n = ", n)
    centers = np.ones(shape=(k, n), dtype=float)
    curr_iteration = prev_iteration = np.zeros(m)
    Min = np.min(X, axis=0)
    Max = np.max(X, axis=0)
    for i in range(k):
        for j in range(n):
            centers[i][j] = random.uniform(Min[j], Max[j])
    curr_iteration = class_of_each_point(X, centers)
    print(prev_iteration)
    print(curr_iteration)

    while True:
        prev_iteration = curr_iteration
    
    #вычисляем новые центры масс
        for i in range(k):
            sub_X = X[curr_iteration == i,:]
            if len(sub_X) > 0:
                centers[i,:] = np.mean(sub_X, axis=0)

    #приписываем каждую точку к заданному классу
        curr_iteration = class_of_each_point(X, centers)
        if np.all(prev_iteration == curr_iteration):
            return centers
    return centers