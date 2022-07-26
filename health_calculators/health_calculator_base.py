
from datetime import datetime
import os
from health_calculators.health_calculator_interface import HealthCalculatorInterface

# base class is needed because 2 methods are the same for all calculators
class HealthCalculatorBase(HealthCalculatorInterface):
    def __init__(self, name):
        # calls the parent class constructor
        super().__init__(name)

    def person(self, person):
        self.person = person
# welcome and save methods are the save for all calculators

    def welcome(self, name):
        print("Welcome %s to my %s calculator !\n" %
              (self.person.name, self.name))

    def save(self, indicator):
        """save save indicator to text file

        Args:
            indicator (float): indicator value
        """        ''''''
        now = datetime.now()
        today_str = now.strftime("%d-%m-%Y")
        document_path = os.path.expanduser('~\Documents')
        f = open(document_path + "\\" + self.person.name +
                 "_" + self.name + "_" + today_str + ".txt", "w")
        f.write(indicator)
        f.close()
