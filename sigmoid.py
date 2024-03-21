import numpy as np
import tensorflow as tf

def sigmoid(z):
    return 1 / (1 + np.exp(-z))
