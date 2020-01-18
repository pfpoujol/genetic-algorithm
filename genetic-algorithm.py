import string
import random

PHRASE_CIBLE = "Omae wa mō shinde iru. NANI ?!!"

class Generation:
    def __init__(self, nb_individus, proportion_elu = 0.5):
        self.nb_individus = int(nb_individus)
        self.proportion_elu = proportion_elu
        self.individus = self._first_generation()

    def _first_generation(self):
        generation = []
        for i in range(0, self.nb_individus):
            generation.append(Individu())
        # To sort the list in place...
        generation.sort(key=lambda individu: individu.fitness, reverse=True)
        return generation

    def find_master_race(self):
        count_cycle = 0
        while self.individus[0].fitness != 1.0:
            count_cycle += 1
            self._next_generation()
            # print(self.individus[0].phrase, end = '\r')
            print(self.individus[0].phrase)
        print("Found in " + str(count_cycle) + " cycles.")


    def _next_generation(self):
        def copulage(phrase1, phrase2):
            child_individu = None
            if len(phrase1) == len(phrase2):
                len_portion_left = int(random.randrange(len(phrase1)-1))
                new_phrase = phrase1[:len_portion_left-1] + phrase2[len_portion_left-1:]
                child_individu = Individu(new_phrase)
            else:
                print("error: copulage(), not same length")
            return child_individu

        def other_individus_elu(individus, index_excluded_indiv):
            return individus[:index_excluded_indiv] + individus[index_excluded_indiv + 1:]

        nb_individus_elu = int(self.nb_individus * self.proportion_elu)
        individus_elu = self.individus[:nb_individus_elu]
        self.individus = []
        newIndividus = []
        i = 0
        while (i < self.nb_individus) :
            for individu in individus_elu:
                if(i == self.nb_individus):
                    break
                # list des partenaire sexuel, on retire l'individu actuel, il ne peut pas copuler tout seul.
                potential_sex_friends = other_individus_elu(individus_elu, i)
                sex_friend = random.choice(potential_sex_friends)
                self.individus.append(copulage(individu.phrase, sex_friend.phrase))
                i += 1

        self.individus.sort(key=lambda individu: individu.fitness, reverse=True)
        #self.individus = newIndividus


class Individu:
    LETTERS = string.printable+"àçèéùîôêâäëïÈÉÀÇÙō?"
    def __init__(self, phrase=None):
        if phrase is None:
            self.phrase = self._gen_random_phrase()
        else:
            # self.phrase = self._mutation(phrase)
            self.phrase = phrase
        self.fitness = self._calculFitness()



    def _gen_random_phrase(self):
        myString = ""
        for i in range(0, len(PHRASE_CIBLE)):  # range(a,b,c) parcourt les valeurs de a à b avec un pas de c
            # myString += random.choice(string.printable+"àçèéùîôêâäëïÈÉÀÇÙ")
            myString += self._randomLetter()
        return myString

    def _calculFitness(self):
        fitness = 0
        if len(self.phrase) == len(PHRASE_CIBLE):
            numerateur = 0.0
            # comparaison char par char
            for x, y in zip(self.phrase, PHRASE_CIBLE):
                if x == y:
                    numerateur += 1
            fitness = numerateur / len(self.phrase)
        else:
            print("error: calculFitness(), not same length")
        return fitness

    def _mutation(self, phrase):
        # 1 chance sur 2 qu'il y ait mutation
        if random.randrange(0) == 0:
            randomRange = int(random.randrange(len(phrase)-1))
            randomLetter = self._randomLetter()
            phrase = phrase[:randomRange] + randomLetter + phrase[randomRange+1:]
        return phrase

    def _randomLetter(self):
        return random.choice(self.LETTERS)


def main():
    generation = Generation(499)
    #generation._next_generation()
    generation.find_master_race()
    i = 1
    for individu in generation.individus:
        print("phrase n° : " + str(i))
        print(individu.phrase)
        print('fitness : ' + str(individu.fitness))
        print("*******************")
        i += 1


if __name__ == '__main__':
    main()
