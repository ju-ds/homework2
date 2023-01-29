"""
Создадим класс Car и метод set_engine
"""

import variables
from base_vehicle import BaseVehicle
from engine import Engine
from variables import FUEL_COMSUMPTION

class Car(BaseVehicle):
    def __init__(self, weight=None, started=0, fuel=None, fuel_consumption=FUEL_COMSUMPTION, engine=None):
        super().__init__(weight=None, started=0, fuel=None, fuel_consumption=FUEL_COMSUMPTION)
        self.engine = engine

    def set_engine(self, engine):
        self.engine = Engine()



