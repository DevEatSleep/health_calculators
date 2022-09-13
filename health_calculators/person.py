
class Person:
    # constructor with 1 parameter
    # self means pointer to the class instance
    def __init__(self, name):
        self.name = name
        self.__height = float()
        self.__weight = float()

    def get_ideal_weight_factor(self):
        pass

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def set_weight(self, weight):
        self.__weight = weight

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def set_height(self, height):
        self.__height = height
