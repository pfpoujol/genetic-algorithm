from abstract_individu import AbstractIndividu

class IndividuItineraire(AbstractIndividu):
    def _gen_random_phrase(self):
        super()._gen_random_phrase()

    def _calcul_fitness(self):
        super()._calcul_fitness()

    def _mutation(self, proba_mutation, phrase):
        super()._mutation(proba_mutation, phrase)

    def _random_letter(self, excluded_letter):
        super()._random_letter(excluded_letter)

    def do_something(self):
        super().do_something()
        print("Things for inividual itinéraire")