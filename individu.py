import string
import random


class Individu:
    PHRASE_CIBLE = "Omae wa mō shinde iru. NANI ?!!"
    LETTERS = string.printable+"àçèéùîôêâäëïÈÉÀÇÙō"
    # LETTERS = string.ascii_letters+" ō?!."
    def __init__(self, proba_mutation=0.0, phrase=None):
        if phrase is None:
            self.phrase = self._gen_random_phrase()
        elif(proba_mutation==0.0):
            self.phrase = phrase
        else:
            self.phrase = self._mutation(proba_mutation, phrase)

        self.fitness = self._calcul_fitness()


    def _gen_random_phrase(self):
        myString = ""
        for i in range(0, len(Individu.PHRASE_CIBLE)):  # range(a,b,c) parcourt les valeurs de a à b avec un pas de c
            myString += self._random_letter(excluded_letter=None)
        return myString

    def _calcul_fitness(self):
        fitness = 0
        if len(self.phrase) == len(Individu.PHRASE_CIBLE):
            numerateur = 0.0
            # comparaison char par char
            for x, y in zip(self.phrase, Individu.PHRASE_CIBLE):
                if x == y:
                    numerateur += 1
            fitness = numerateur / len(self.phrase)
        else:
            print("error: calculFitness(), not same length")
        return fitness

    def _mutation(self, proba_mutation, phrase):
        if random.random() < proba_mutation:
            randomRange = int(random.randrange(len(phrase)))
            randomLetter = self._random_letter(phrase[:randomRange])
            phrase = phrase[:randomRange] + randomLetter + phrase[randomRange+1:]
        return phrase

    def _random_letter(self, excluded_letter):
        letter = None
        if excluded_letter is None:
            letter = random.choice(Individu.LETTERS)
        else:
            letter = random.choice(Individu.LETTERS.replace(excluded_letter, ""))
        return letter