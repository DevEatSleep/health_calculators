import os
from datetime import datetime

from config import parse

from health_calculators.health_calculator_base import HealthCalculatorBase
from health_calculators.man import Man
from health_calculators.woman import Woman


class IbwCalculator(HealthCalculatorBase):
    def __init__(self):
        super().__init__("IBW")

    def person(self, person):
        self.person = person

    def welcome(self, name):
        super().welcome(name)
    
    def input_parameters(self):
        gender = str(input("Are you a woman (1) or a man (2) ?\n"))
        if(gender == "1"):
            self.person = Woman(self.person.name)
        if(gender == "2"):
            self.person = Man(self.person.name)
        self.person.set_height = float(
            input("Please input your height in cm: ")) 
        self.person.set_weight = float(input("and your weight in kg: "))      

    def calc(self):
        # raise a specific error if values are not correct
        if self.person.height < 0:
            raise ValueError("Sorry, no numbers below zero")
        else:           
            factor = self.person.ideal_weight_factor
        # Lorentz formula
            ibw = (self.person.height - 100) - ((self.person.height - 150) / factor)
            return ibw

    def analyze(self, current_weight, ideal_weight):
        if current_weight > ideal_weight:
            return "Sorry, you're overweight"
        if current_weight <= ideal_weight:
            return "Cool, you're not overweight!"

    def save(self, ibw):
       super().save(ibw)
