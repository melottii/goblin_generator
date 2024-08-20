# source /home/melot/.virtualenvs/goblin_generator/bin/activate
from app.builders.characterBuilder import CharacterBuilder

class GoblinGenerator:
    def __init__(self):
        self.character = CharacterBuilder()

    def __print_personagem__(self):
        print("Nome: ", self.character.name)
        print("Aparência: ", self.character.appearance)
        print("Ocupação: ", self.character.occupation)
        print("Nível: ", self.character.level)
        print("Status: ", self.character.status)
        print("Equipamento: ", self.character.equipment)
        print("Vitalidade: ", self.character.vitality)
        print("Dano: ", self.character.damage)
        print("Proteção: ", self.character.protection)


if __name__ == "__main__":
    goblin = GoblinGenerator()
    goblin.character = goblin.character.director(name="Paiaço", color="")
    goblin.__print_personagem__()