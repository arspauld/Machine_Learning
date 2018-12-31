from sklearn import datasets
import numpy as np

digits = datasets.load_digits()

print(digits.data)

def __sigmoid(x):
    return 1/(1+np.exp(-x))

def __sigmoid_derivative(x):
    

print(__sigmoid(-200))