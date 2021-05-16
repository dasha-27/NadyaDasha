import numpy as np

#евклидово расстояние между двумя точками
def dist(A, B):
    if len(A) != len(B):
        raise Exception('Размеры массивов не совпадают')
    return np.sqrt(np.sum([(A[i] - B[i]) ** 2 for i in range(len(A))]))

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
    centers = np.ones(shape=(k, n), dtype=float)
    curr_iteration = prev_iteration = np.zeros(m)
    centers = np.random.uniform(np.min(X, axis=0), np.max(X, axis=0), (k, n))
    curr_iteration = class_of_each_point(X, centers)

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
