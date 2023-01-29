"""
Создадим базовый класс и основные методы

"""
import variables
from variables import FUEL_COMSUMPTION
from exceptions import LowFuelError, NotEnoughFuel, CargoOverload

class BaseVehicle():
    def __init__(self, weight=None, started=0, fuel=None, fuel_consumption=FUEL_COMSUMPTION):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        if not (self.started == 0 and self.fuel > 0):
            #print(f'Started status is now: {self.started} Not Started')
            self.started = 0
            raise LowFuelError(f'Fuel is {self.fuel}')
        else:
            self.started = 1
            #print(f'Started status is now: {self.started} (Started)')


    def move(self, distance):
        fuel_needs =  (self.fuel_consumption * distance)/100
        if not (self.fuel >= fuel_needs):
            raise NotEnoughFuel(f'Fuel ({self.fuel} l) is less than needed ({fuel_needs} l)')
        else:
            self.fuel -= fuel_needs
            print(f'There is enough fuel ({fuel_needs} l) for this distance : {distance}')







#    def start(self):
#        if (self.started == 0 and self.fuel == 0):
#            self.started = 0
#            #print(f'Started status is now: {self.started} Not Started')
#            raise LowFuelError(f'Fuel is {self.fuel}')
#        elif (self.started == 1 and self.fuel == 0):
#            self.started = 1
#            #print(f'Started status is now: {self.started} Not Started')
#           raise LowFuelError(f'Fuel is {self.fuel}')
#        elif (self.started == 0 and self.fuel > 0):
#            #print(f'Started status is now: {self.started} Started')
#            self.started = 1
#        else:
#            self.started = 1
#            #print(f'Started status is now: {self.started} (Started)')




