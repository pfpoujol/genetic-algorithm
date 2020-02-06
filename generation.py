import time
import random
from individu import Individu


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
                len_portion_left = int(random.randrange(len(phrase1)))
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
        start_time = time.time()
        count_cycle = 0
        while self.individus[0].fitness != 1.0:
            count_cycle += 1
            self._next_generation(proba_mutation)
            print(self.individus[0].phrase)
        print("--- Found in %s seconds ---" % round((time.time() - start_time),3))
        print("--- After " + str(count_cycle) + " cycles.")
        return count_cycle