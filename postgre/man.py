from health_calculators.person import Person


class Man(Person):
    def __init__(self, name):
        super().__init__(name)
        self._ideal_weight_factor = 4

    @property
    def ideal_weight_factor(self):
        return self._ideal_weight_factor   

    @property
    def height(self):
        return super().height

    @property
    def weight(self):
        return super().weight
