"""
Создадим класс Plane и метод load_cargo
"""
import variables
from base_vehicle import BaseVehicle
from exceptions import CargoOverload
from variables import FUEL_COMSUMPTION, MAX_CARGO


class Plane(BaseVehicle):
    def __init__(self, weight=None, started=0, fuel=None, fuel_consumption=FUEL_COMSUMPTION, cargo = 0, max_cargo=MAX_CARGO):
        super().__init__(weight=None, started=0, fuel=None, fuel_consumption=FUEL_COMSUMPTION)
        self.cargo = cargo
        self.max_cargo = MAX_CARGO


    def load_cargo(self, new_cargo):
        cargo_upd = self.cargo + new_cargo
        if not (cargo_upd <= MAX_CARGO):
            raise CargoOverload(f'Cargo ({cargo_upd}) is more than Max_Cargo ({MAX_CARGO})')
        else:
            self.cargo = cargo_upd


    def remove_all_cargo(self):
        pass
