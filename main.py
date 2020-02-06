from generation import Generation


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
    # Generation(100, proportion_elu=0.1).find_master_race(proba_mutation=0.1)
    list_result.append(Generation(500, proportion_elu=0.5).find_master_race(proba_mutation=0.2))

if __name__ == '__main__':
    main()
