from abc import abstractmethod

from app.factory.characterFactory import CharacterFactory


class CharacterBuilder:
    @abstractmethod
    def director(self, name, color):
        fabrica_personagem = CharacterFactory()
        fabrica_personagem.__set_name__(name=name)
        fabrica_personagem.__set_color__(color=color)
        return fabrica_personagem
