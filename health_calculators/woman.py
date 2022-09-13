from health_calculators.person import Person


class Woman(Person):
    def __init__(self, name):
        super().__init__(name)
        # naming convention for private variable with two _ at the beginning 
        # and one _ for protected variable
        self.__ideal_weight_factor = 2

    @property
    def ideal_weight_factor(self):
        return self.__ideal_weight_factor

    # getter is to read the value of the private variable
    # in Python, private or protected access doesn't exist
    # variables are public to caller
    @ideal_weight_factor.getter
    def get_ideal_weight_factor(self) -> int:
        return self.__ideal_weight_factor

    @property
    def height(self) -> float:
        return super().height

    @property
    def weight(self) -> float:
        return super().weight
