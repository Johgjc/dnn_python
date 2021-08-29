import matrix
import vector
import activate as act


class DNNLayer:
    def __init__(self):
        self.__input = None
        self.__output = None
        self.__bias = None
        self.__weight = None
        self.__activate = None
        self.__row = 0
        self.__col = 0
        self.__dropout = 0.0

    def __getattr__(self, _item):
        if _item == "input":
            return self.__input
        elif _item == "output":
            return self.__output
        elif _item == "bias":
            return self.__bias
        elif _item == "weight":
            return self.__weight
        elif _item == "activate":
            return self.__activate
        elif _item == "row" or _item == "output_size":
            return self.__row
        elif _item == "col" or _item == "input_size":
            return self.__col
        elif _item == "dropout":
            return self.__dropout
        else:
            return

    def init_layer(self, _input_size, _output_size, _activate, _dropout=0.0):
        self.__row = _output_size
        self.__col = _input_size
        self.__input = vector.generate(self.__col)
        self.__output = vector.generate(self.__row)
        self.__weight = matrix.generate(self.__row, self.__col)
        self.__bias = vector.generate(self.__row)
        self.set_activate(_activate)
        self.__dropout = 0.0

    def set_weight(self, _weight):
        self.__weight = _weight

    def set_bias(self, _bias):
        self.__bias = _bias

    def set_dropout(self, _dropout):
        self.__dropout = _dropout

    def set_activate(self, _activate):
        self.__activate = act.activate_map(_activate)

    def calculate(self, _input):
        self.__input = _input
        self.__output = self.__activate(self.__weight * self.__input + self.__bias)
        return self.__output

    def backpropagation(self):
        pass


class DNNModel:
    def __init__(self):
        self.input = None
        self.output = None
        self.layers = []

    def init_model(self):
        pass

    def run(self, _input):
        if not isinstance(_input, vector.Vector):
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


def test_dnn_layer():
    layer1 = DNNLayer()
    layer1.row = 1
    layer1.col = 1
    layer1.input = vector.generate(4, True)
    layer1.output = vector.generate(3, True)
    layer1.weight = matrix.generate(3, 4, True)
    layer1.bias = vector.generate(3, True)
    layer1.set_activate("linear")
    layer1.dropout = 0.0
    layer1.calculate(layer1.input)
    print("input {}".format(layer1.input))
    print("weight {}".format(layer1.weight))
    print("bias {}".format(layer1.bias))
    print("output {}".format(layer1.output))

    layer2 = DNNLayer()
    layer2.init_layer(5, 12, "softmax")


if __name__ == '__main__':
    test_dnn_layer()
