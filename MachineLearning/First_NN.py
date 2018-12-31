from sklearn import datasets
import numpy as np

digit = datasets.load_digits()

def __sigmoid(x):
    return 1/(1+np.exp(-x))

def __sigmoid_derivative(x):
    print('sigmoid derivative\n')

print(__sigmoid(-200))
