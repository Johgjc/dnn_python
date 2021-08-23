from matrix import Matrix
from vector import Vector
import activate


class DNNDesc:
    def __init__(self):
        self.layer_count = 0
        self.activate = []
        self.input_size = []
        self.output_size = []


class DNNLayer:
    def __init__(self):
        self.input = Vector()
        self.output = Vector()
        self.bias = Vector()
        self.weight = Matrix()
        self.activate = None
        self.row = 0
        self.col = 0


class DNNModel:
    def __init__(self):
        self.input = Vector()
        self.output = Vector()
        self.layers = []
        self.desc = DNNDesc()
