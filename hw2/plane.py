"""
Создадим класс Plane и метод load_cargo
"""
import variables
from base_vehicle import BaseVehicle
from exceptions import CargoOverload
from variables import FUEL_COMSUMPTION, MAX_CARGO


class Plane(BaseVehicle):
    def __init__(self, weight=None, started=0, fuel=None, fuel_consumption=FUEL_COMSUMPTION, cargo = 0, max_cargo=MAX_CARGO):
        super().__init__(weight=None, fuel=None, fuel_consumption=FUEL_COMSUMPTION)
        self.cargo = cargo
        self.max_cargo = MAX_CARGO
        self.started = False


    def load_cargo(self, new_cargo):
        cargo_upd = self.cargo + new_cargo
        if cargo_upd < MAX_CARGO:
            self.cargo = cargo_upd
        else:
            raise CargoOverload(f'Cargo ({cargo_upd}) is more than Max_Cargo ({MAX_CARGO})')


    def remove_all_cargo(self):
         cargo_previous= self.cargo
         self.cargo = 0
         return cargo_previous
