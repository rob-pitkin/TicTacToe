import numpy as np
import math

class Node:
    def __init__(self):
        self.input_weights = None
        self.bias = None

class NeuralNet:
    def __init__(self, num_inputs, num_outputs, num_hidden, num_layers):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.num_hidden = num_hidden 
        self.num_layers = num_layers

    # Here are two activation functions, as sigmoid has been phased
    # out of usage as of late
    def sigmoid_function(self, x):
        return 1 / (1 + math.pow(math.e, -x))
    
    def relu_function(self, x):
        return max(0,x)