import numpy as np


def get_exponential_distributed_number(l):
    return -np.log(np.random.uniform()) / l


def transform_uniform_to_exponential_distribution(p, l):
    return -(1. / l) * np.log(p)
