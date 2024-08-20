from abc import ABC

import random
import re
import sys

from unidecode import unidecode

from app.factory.resources.colors import LightGreen, DarkGreen, Green, Red, Yellow, Blue
# from app.resources.racas import halfling_pes_leves, halfling_robusto, anao_colina, anao_montanha
# from app.resources.antecedentes import acolito, artesaoDeGuilda, charlatao


class CharacterFactory(ABC):
    def __init__(self):
        self.name = ""
        self.color = ""
        self.appearance = ""
        self.occupation = ""
        self.level = 0
        self.status = {
            "fight": 0,
            "knowledge": 0,
            "skill": 0,
            "luck": 0
        }
        self.equipment = []
        self.vitality = 0
        self.damage = 0
        self.protection = 0

    def __set_name__(self, name: str):
        self.name = name

    def __set_color__(self, color: str):
        try:
            choices = ["VERDE", "VERDE ESCURO", "VERDE CLARO", "AMARELO", "VERMELHO", "AZUL"]
            if color.upper() == "":
                color = random.choice(choices)
            else:
                color = re.sub("[0-9]", "", unidecode(color.upper()))
                if color not in choices:
                    color = random.choice(choices)
            match color:
                case "VERDE":
                    self.color = Green()
                case "VERDE ESCURO":
                    self.color = DarkGreen()
                case "VERDE CLARO":
                    self.color = LightGreen()
                case "AMARELO":
                    self.color = Yellow()
                case "VERMELHO":
                    self.color = Red()
                case "AZUL":
                    self.color = Blue()
            self.color.__set_config__(character=self)
        except Exception as e:
            sys.exit(f"ERRO AO DEFINIR COR DO PERSONAGEM: {e}")
