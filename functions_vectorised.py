import numpy as np
from typing import Tuple


def sum_non_neg_diag(X: np.ndarray) -> int:
    diag = np.diag(X)
    if(np.all(diag < 0)):
        return -1
    else:
        return sum(diag)

def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    return all(np.sort(x) == np.sort(y))


def max_prod_mod_3(x: np.ndarray) -> int:
    y = (np.append(x, 0))[1:]
    xy = x * y
    out = max(np.where(xy % 3 == 0, xy, 0))
    return out if out != 0 else -1

def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    return np.sum(np.multiply(image, weights), axis=2)


def rle_scalar(x: np.ndarray, y: np.ndarray) -> int:
    outx = np.repeat(x[:, 0], x[:, 1])
    outy = np.repeat(y[:, 0], y[:, 1])
    return np.dot(outx, outy) if len(outx) == len(outy) else -1


def cosine_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    return np.nan_to_num(np.matmul(X, Y.T) / np.outer(np.linalg.norm(X, axis=1), np.linalg.norm(Y, axis=1)), nan=1)
