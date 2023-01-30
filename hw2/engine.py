"""
Создадим датакласс Engine
"""
from dataclasses import dataclass

@dataclass
class Engine():
    volume: int = 1600
    pistons: int = 4


#def __init__(self, volume: int, pistons: int):
#       self.volume = volume
#        self.pistons = pistons
