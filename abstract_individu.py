import string
from abc import ABC, abstractmethod
class AbstractIndividu(ABC):
    PHRASE_CIBLE = "Omae wa mō shinde iru. NANI ?!!"
    LETTERS = string.printable + "àçèéùîôêâäëïÈÉÀÇÙō"

    def __init__(self, proba_mutation=0.0, phrase=None):
        self.phrase = phrase
        self.proba_mutation = proba_mutation
        super().__init__()

    @abstractmethod
    def _gen_random_phrase(self):
        pass

    @abstractmethod
    def _calcul_fitness(self):
        pass

    @abstractmethod
    def _mutation(self, proba_mutation, phrase):
        pass

    @abstractmethod
    def _random_letter(self, excluded_letter):
        pass

    @abstractmethod
    def do_something(self):
        print("Some implementation!")

