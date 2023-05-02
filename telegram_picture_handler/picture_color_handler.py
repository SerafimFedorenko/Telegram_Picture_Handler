from sklearn.cluster import KMeans
from PIL import Image, ImageChops
import numpy as np


def handle_picture(path, n_colors):
    test_img = Image.open(path)
    test_x = np.array(test_img, np.float32)
    x_f = test_x / 255.0
    height = len(x_f)
    width = len(x_f[0])
    bw = False
    if type(x_f[0][0]) == np.ndarray or type(x_f[0][0]) == list:
        x_train = x_f.reshape(-1, len(x_f[0][0]))
    else:
        x_train = x_f.reshape(-1, 1)
        bw = True
    model = KMeans(n_clusters=n_colors, random_state=10).fit(x_train)
    centroids = model.cluster_centers_
    y_pred = model.predict(x_train)
    x_new = []
    for y in y_pred:
        if bw:
            x_new.append([centroids[y].tolist()[0], centroids[y].tolist()[0], centroids[y].tolist()[0]])
        else:
            x_new.append(centroids[y].tolist())
    x_n = np.array(x_new).reshape((height, width, -1))
    img = Image.fromarray((x_n * 255).astype(np.uint8))

    return img


def get_gamma(path, n_colors):
    test_img = Image.open(path)
    test_x = np.array(test_img, np.float32)
    x_f = test_x / 255.0
    height = len(x_f)
    width = len(x_f[0])
    x_train = x_f.reshape(-1, 3)
    model = KMeans(n_clusters=n_colors, random_state=10).fit(x_train)
    centroids = model.cluster_centers_

    x_new = []
    for i in range(100):
        for centroid in centroids:
            for j in range(100):
                x_new.append(centroid.tolist())

    x_n = np.array(x_new).reshape((100, 100 * n_colors, -1))
    img = Image.fromarray((x_n * 255).astype(np.uint8))

    return img
