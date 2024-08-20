from abc import ABC


class LightGreen(ABC):
    def __init__(self):
        self.status = {
            "fight": 2,
            "knowledge": 2,
            "skill": 1,
            "luck": 1
        }

    def __set_config__(self, character):
        for status in self.status:
            character.status[status] = character.status[status] + self.status[status]
        character.color = "VERDE CLARO"


class DarkGreen(ABC):
    def __init__(self):
        self.status = {
            "fight": 2,
            "knowledge": 1,
            "skill": 2,
            "luck": 1
        }

    def __set_config__(self, character):
        for status in self.status:
            character.status[status] = character.status[status] + self.status[status]
        character.color = "VERDE ESCURO"

class Red(ABC):
    def __init__(self):
        self.status = {
            "fight": 1,
            "knowledge": 2,
            "skill": 2,
            "luck": 1
        }

    def __set_config__(self, character):
        for status in self.status:
            character.status[status] = character.status[status] + self.status[status]
        character.color = "VERMELHO"

class Green(ABC):
    def __init__(self):
        self.status = {
            "fight": 2,
            "knowledge": 1,
            "skill": 1,
            "luck": 2
        }

    def __set_config__(self, character):
        for status in self.status:
            character.status[status] = character.status[status] + self.status[status]
        character.color = "VERDE"

class Yellow(ABC):
    def __init__(self):
        self.status = {
            "fight": 1,
            "knowledge": 1,
            "skill": 2,
            "luck": 2
        }

    def __set_config__(self, character):
        for status in self.status:
            character.status[status] = character.status[status] + self.status[status]
        character.color = "AMARELO"

class Blue(ABC):
    def __init__(self):
        self.status = {
            "fight": 1,
            "knowledge": 2,
            "skill": 1,
            "luck": 2
        }

    def __set_config__(self, character):
        for status in self.status:
            character.status[status] = character.status[status] + self.status[status]
        character.color = "AZUL"
