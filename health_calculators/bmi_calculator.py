import os
import psycopg2
from datetime import datetime
from config import parse
from health_calculators.health_calculator_base import HealthCalculatorBase

# OOP inheritance 
class BmiCalculator(HealthCalculatorBase):
    def __init__(self):
# calls the parent class constructor
        super().__init__("BMI")

    def person(self, person):
        self.person = person

    def welcome(self, name):
        super()._welcome(name)
       
    def input_parameters(self):
        """input_parameters get the parameters for bmi calculation
        """        ''''''
        self.person.set_height = float(
            input("Please input your height in cm: "))
        self.person.set_weight = float(input("and your weight in kg: "))

    def calc(self) -> float:
        """calc the bmi calculation

        Raises:
            ValueError: if numbers are below 0

        Returns:
            float: the value of the indicator
        """        ''''''
        # raise a specific error if values are not correct
        if self.person.weight < 0 or self.person.height < 0:
            raise ValueError("Sorry, no numbers below zero")
        else:
            # '**2' means power
            bmi = self.person.weight / (self.person.height/100)**2
            return bmi

    def analyze(self, bmi, calculator_table) -> str:
        """analyze display a message corresponding to the bmi value


        Args:
            bmi (float): the indicator value
            calculator_table (dict): a table providing messages when bmi is in a range

        Returns:
            str: the message
        """               
        params = parse("database.ini", "postgresql")
        try:
            # **params means unpacking dictionary
            connection = psycopg2.connect(**params)
            cursor = connection.cursor()
            cursor.execute("SELECT message FROM " + calculator_table +
                           " WHERE " + str(bmi) + " BETWEEN min AND max")
            message = cursor.fetchone()

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    # *message means unpacking tuple
            return str(*message)

    def save(self, bmi):       
        super()._save(bmi)