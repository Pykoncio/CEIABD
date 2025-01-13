import numpy as np

class Neuron: # Usamos todo el rato el self para referirnos a los atributos y metodos de la clase
    def __init__(self, weights, bias, activation_function_name="sigmoid"): # Sigmoid es por defecto
        self.__weights = weights
        self.__bias = bias
        self.__activation_function = self.__get_activation_function(activation_function_name)

    @property
    def weights(self):
        return self.__weights
    
    @weights.setter
    def weights(self, weights):
        self.__weights = weights

    @property
    def bias(self):
        return self.__bias
    
    @bias.setter
    def bias(self, bias):
        self.__bias = bias

    def __get_activation_function(self, name):
        
        functions = {
            "sigmoid": self.__sigmoid,
            "relu": self.__relu,
            "tanh": self.__tanh,
            "binary_step": self.__binary_step
        }

        return functions.get(name, self.__sigmoid) # Si no encuentra la función, devuelve la sigmoide
    
    def __sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def __tanh(self, x):
        return np.tanh(x)

    def __relu(self, x):
        return np.maximum(0, x)
    
    def __binary_step(self, x):
        return np.where(x >= 0, 1, 0)
    
    def run(self, input_data):
        if len(input_data) != len(self.__weights):
            raise ValueError(f"El número de entradas y pesos no coincide... El vector de entrada debe de tener una longitud de {len(self.weights)} valores.")
        else:
            y = np.dot(input_data, self.__weights) + self.__bias
            return self.__activation_function(y)