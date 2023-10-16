from typing import List


def sum_non_neg_diag(X: List[List[int]]) -> int:
    out = 0
    flag = False
    for i in range(min(len(X), len(X[1]))):
        if (X[i][i] >= 0):
            flag = True
            out += X[i][i]
    if flag:
        return out
    else:
        return -1


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    return(sorted(x) == sorted(y))


def max_prod_mod_3(x: List[int]) -> int:
    out = -1
    for i in range(len(x) - 1):
        if((x[i] % 3 == 0 or x[i+1] % 3 == 0) and x[i] * x[i + 1] > out):
            out = x[i] * x[i+1]
    return out


def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    out = [[0 for width in range(len(image[0]))] for height in range(len(image))]
    for height in range(len(image)):
        for width in range(len(image[height])):
            for num_channels in range(len(image[height][width])):
                out[height][width] += image[height][width][num_channels] * weights[num_channels]
    return out

def rle_scalar(x: List[List[int]], y:  List[List[int]]) -> int:
    x_trans = []
    for i in range(len(x)):
        for j in range(x[i][1]):
            x_trans.append(x[i][0])
    y_trans = []
    for i in range(len(y)):
        for j in range(y[i][1]):
            y_trans.append(y[i][0])
    return -1 if (len(y_trans) != len(x_trans)) else sum([x_trans[i] * y_trans[i] for i in range(len(x_trans))])

def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    out = [[0 for i in range(len(X[0]))] for i in range(len(X))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            if(any(X[i]) and any(Y[j])):
                out[i][j] = sum([X[i][jj] * Y[j][jj] for jj in range(len(Y[j]))]) / ((sum([X[i][jj] ** 2 for jj in range(len(Y[j]))]) ** 0.5) * (sum([Y[j][jj] ** 2 for jj in range(len(Y[j]))]) ** 0.5))
            else:
                out[i][j] = 1
    return out


