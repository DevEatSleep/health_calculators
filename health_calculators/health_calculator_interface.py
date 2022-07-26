from abc import ABC, abstractmethod
from multipledispatch import dispatch

# OOP polymorphism at a class level
# interface is just entry points, implementation is in derived classes
class HealthCalculatorInterface(ABC):
    def __init__(self, name):
        self._name = name

# OOP encapsulation 
# @property hides the private variable (not really hidden in Python)
    @property
    def name(self):
        return self._name
# getter is to read property value (getter keyword is optional)
    @property
    def person(self):
        return self._person
# setter is to set property value
    @person.setter
    def set_person(self, person):
        self._person = person

    @abstractmethod
    def welcome(self, name):
        pass

    @abstractmethod
    def input_parameters(self):
        pass

# abstract method is a method without code, implementation is in derived class
    @abstractmethod
    def calc(self):
        pass

# OOP polymorphism at a method level, need package 'multipledispatch'
# method overloading (different signatures) 
    @dispatch(str, str)
    @abstractmethod
    def analyze(self, result, calculator_table):
        pass

    @dispatch(float, float)
    @abstractmethod
    def analyze(self, current_weight, ideal_weight):
        pass

    @abstractmethod
    def save(self, result):
        pass
