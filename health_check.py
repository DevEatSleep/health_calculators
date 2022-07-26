from logging import exception
import os

from config import parse
from health_calculators.person import Person
from to_object import *

# lambda allows simple inline method
cls = lambda: os.system('cls' if os.name=='nt' else 'clear')

# entry point  of the program

def main():

    # error handling
    try:
        calculator = object()
        cls()
        name = str(input("Hi, what's your name ?\n"))
        person = Person(name)
        calc_choice = str(
            input("Do you want to calculate your Body Mass Index (1) or Ideal Body Weight (2) ?\n"))

        if int(calc_choice) > 2:
            print("No others calculators implemented")
            return
        else:
            calculator_config = parse("calculators.ini", calc_choice)
            if 'calculator_table' in calculator_config:
                calculator_table = calculator_config['calculator_table']
            # object is dynamically created with the class name founded in an ini file
            calculator = create_instance(
                calculator_config['calculator_name'] + "()")
            calculator.person = person

        calculator.welcome(name)
        calculator.input_parameters()

        health_indicator = calculator.calc()
        result_message = "Your %s is %.2f" % (calculator.name, health_indicator)
        print(result_message)
# check the existence of a local variable
        if 'calculator_table' in locals():
        # differents analyze methods are only implemented to demonstrate overloading, 
        # this could be replaced in a better way by an analyzer interface          
            status_msg = calculator.analyze(health_indicator, calculator_table)
        else:
            status_msg = calculator.analyze(calculator.person.weight, health_indicator)
        if status_msg:
            print(status_msg)

        calculator.save(str(health_indicator))

    except ValueError:
        print(ValueError.args)
    except exception:
        print("An exception occurred")
    finally:
        print("Bye")

if __name__ == "__main__":
    main()