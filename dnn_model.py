from matrix import Matrix
from vector import Vector
import activate as act


class DNNLayer:
    def __init__(self):
        self.input = Vector()
        self.output = Vector()
        self.bias = Vector()
        self.weight = Matrix()
        self.activate = None
        self.row = 0
        self.col = 0
        self.dropout = 0.0

    def init_layer(self):
        pass

    def set_activate(self, _activate):
        self.activate = act.activate_map(_activate)

    def calculate(self, _input):
        self.output = _input

        return self.output

    def backpropagation(self):
        pass


class DNNModel:
    def __init__(self):
        self.input = Vector()
        self.output = Vector()
        self.layers = []

    def init_model(self):
        pass

    def run(self, _input):
        if not isinstance(_input, Vector):
            raise ValueError("Wrong input type, a vector is needed.")
        self.input = _input
        self.calculate()
        self.backpropagation()

    def calculate(self):
        self.output = self.input
        for layer in self.layers:
            self.output = layer.calculate(self.output)
        return self.output

    def backpropagation(self):
        for layer in self.layers:
            layer.backpropagation()


def get_dnn_model():
    dnn_model = DNNModel()
    dnn_model.init_model()
    return dnn_model
