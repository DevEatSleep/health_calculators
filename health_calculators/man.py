from health_calculators.person import Person


class Man(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__ideal_weight_factor = 4

    @property
    def ideal_weight_factor(self) -> int:
        return self.__ideal_weight_factor   

    @property
    def height(self) -> float:
        return super().height

    @property
    def weight(self) -> float:
        return super().weight
