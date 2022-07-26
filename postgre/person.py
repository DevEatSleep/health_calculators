
class Person:
    # constructor with 1 parameter
    # self means pointer to the class instance
    def __init__(self, name):
        self.name = name
        self._height = float()
        self._weight = float()

    def get_ideal_weight_factor(self):
        pass

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def set_weight(self, weight):
        self._weight = weight

    @property
    def height(self):
        return self._height

    @height.setter
    def set_height(self, height):
        self._height = height
