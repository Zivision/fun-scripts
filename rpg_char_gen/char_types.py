from dataclasses import dataclass
from enum import Enum


class Race(Enum):
    HUMAN = 1
    ELF = 2
    DWARF = 3
    ORC = 4


class Char_Class(Enum):
    BARD = 1
    WARRIOR = 2
    CLERIC = 3


@dataclass
class Character:
    name: str
    race: Race
    char_class: Char_Class
    backstory: str
