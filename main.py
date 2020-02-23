from generation import Generation
from individu import Individu
from individu_itineraire import IndividuItineraire
from abc import ABC, abstractmethod
def main():
    # IndividuItineraire().do_something()
    Individu().do_something()
    IndividuItineraire().do_something()
    Generation(500, proportion_elu=0.1).find_master_race(proba_mutation=0.9)
if __name__ == '__main__':
    main()
