import numpy as np
import matplotlib.pyplot as plt

def random_population(List_allele, population_size):
    """
    Create a random population
    """
    population = []

    for individu in range(population_size):
        population.append(np.random.choice(List_allele))
        population = sorted(population)

    return population

def wright_fisher(population, generation):

    """
    Generate wright fisher data for each generation
    """
    arr = np.array(population)

    for gen in range(generation):
        population = random_population(population, len(population))
        arr = np.vstack((arr, np.array(population)))

    return arr

def show_result(pop_MATRIX, population_size, generation):
    """
    Plot results for total generations
    """
    dict_pop_evolution = {}
    for row in pop_MATRIX:
        unique, counts = np.unique(row, return_counts=True)
        counts = [number / population_size for number in counts]
        dict_generation_X = dict(zip(unique, counts))

        for key, value in dict_generation_X.items():
            try:
                dict_pop_evolution[key].append(value)
            except:
                dict_pop_evolution[key] = [value]

    for k, v in dict_pop_evolution.items():
        plt.plot(v, label=k)
        plt.xlim([0, generation + generation*0.2])
        plt.xlabel('generations')
        plt.ylabel('Allele frequency')
        plt.ylim([0, 1])
        plt.title('Frequency evolution of multiple alleles in competition with no mutations')
        plt.legend()
        plt.savefig("test.png")
    plt.show()

if __name__ == "__main__":

    #initial data
    allele_ref = ["A", "B", "C", "D", "E"]
    nbr_individus_pop = 500
    generation = 500

    #Run simulation:
    for i in range(1):
        initial_pop = random_population(allele_ref, nbr_individus_pop)

        pop_after_x_gen = wright_fisher(initial_pop, generation)

        show_result(pop_after_x_gen, nbr_individus_pop, generation)
