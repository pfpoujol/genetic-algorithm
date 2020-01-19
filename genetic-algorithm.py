import string
import random

PHRASE_CIBLE = "Omae wa mō shinde iru. NANI ?!!"

class Generation:
    def __init__(self, nb_individus, proportion_elu=0.5):
        self._nb_individus = int(nb_individus)
        self._proportion_elu = proportion_elu
        self.individus = self._first_generation()

    def _first_generation(self):
        generation = []
        for i in range(0, self._nb_individus):
            generation.append(Individu())
        # Tri des individues, le meilleur fitness en haut
        generation.sort(key=lambda individu: individu.fitness, reverse=True)
        return generation


    def _next_generation(self, proba_mutation):
        def copulage(phrase1, phrase2):
            child_individu = None
            if len(phrase1) == len(phrase2):
                len_portion_left = int(random.randrange(len(phrase1)-1))
                new_phrase = phrase1[:len_portion_left-1] + phrase2[len_portion_left-1:]
                child_individu = Individu(proba_mutation, new_phrase)
            else:
                print("error: copulage(), not same length")
            return child_individu

        def other_individus_elu(individus, index_excluded_indiv):
            return individus[:index_excluded_indiv] + individus[index_excluded_indiv + 1:]

        nb_individus_elu = int(self._nb_individus * self._proportion_elu)
        individus_elu = self.individus[:nb_individus_elu]
        self.individus = []
        i = 0
        while (i < self._nb_individus) :
            for individu in individus_elu:
                if(i == self._nb_individus):
                    break
                # list des partenaire sexuel, on retire l'individu actuel, il ne peut pas copuler tout seul.
                potential_sex_friends = other_individus_elu(individus_elu, i)
                sex_friend = random.choice(potential_sex_friends)
                self.individus.append(copulage(individu.phrase, sex_friend.phrase))
                i += 1
        self.individus.sort(key=lambda individu: individu.fitness, reverse=True)

    def find_master_race(self, proba_mutation=0.25):
        count_cycle = 0
        while self.individus[0].fitness != 1.0:
            count_cycle += 1
            self._next_generation(proba_mutation)
            # print(self.individus[0].phrase, end = '\r')
            print(self.individus[0].phrase)
        print("Found in " + str(count_cycle) + " cycles.")
        return count_cycle

class Individu:
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
        for i in range(0, len(PHRASE_CIBLE)):  # range(a,b,c) parcourt les valeurs de a à b avec un pas de c
            # myString += random.choice(string.printable+"àçèéùîôêâäëïÈÉÀÇÙ")
            myString += self._random_letter(excluded_letter=None)
        return myString

    def _calcul_fitness(self):
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

    def _mutation(self, proba_mutation, phrase):
        if random.random() < proba_mutation:
            randomRange = int(random.randrange(len(phrase)-1))
            randomLetter = self._random_letter(phrase[:randomRange])
            phrase = phrase[:randomRange] + randomLetter + phrase[randomRange+1:]
        return phrase

    def _random_letter(self, excluded_letter):
        letter = None
        if excluded_letter is None:
            letter = random.choice(self.LETTERS)
        else:
            letter = random.choice(self.LETTERS.replace(excluded_letter, ""))
        return letter


def main():
    def print_generation(gen):
        i = 1
        for individu in gen.individus:
            print("phrase n° : " + str(i))
            print(individu.phrase)
            print('fitness : ' + str(individu.fitness))
            print("*******************")
            i += 1

    list_result = []
    # list_result.append(Generation(50).find_master_race())
    # list_result.append(Generation(100).find_master_race())
    list_result.append(Generation(500).find_master_race())
    # list_result.append(Generation(1000).find_master_race())
    # list_result.append(Generation(2000).find_master_race())


    print(list_result)

if __name__ == '__main__':
    main()
