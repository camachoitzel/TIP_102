# P1

# Imagine you are working on a wildlife conservation database. Write a function named most_endangered() that returns the species with the highest conservation priority based on its population.

# The function should take in a list of dictionaries named species_list as a parameter. Each dictionary represents data associated with a species, including its name, habitat, and wild population. The function should return the name of the species with the lowest population.

# If there are multiple species with the lowest population, return the species with the lowest index.

# def most_endangered(species_list):
#     pass
# Example Usage:

# species_list = [
#     {"name": "Amur Leopard",
#      "habitat": "Temperate forests",
#      "population": 84
#     },
#     {"name": "Javan Rhino",
#      "habitat": "Tropical forests",
#      "population": 72
#     },
#     {"name": "Vaquita",
#      "habitat": "Marine",
#      "population": 10
#     }
# ]

# print(most_endangered(species_list))
# Example Output:

# Vaquita

# SOLUTION:


def most_endangered(species_list):
    if not species_list:
        return None  # Return None if the list is empty

    lowest_population = float('inf')
    endangered_species = ""

    for species in species_list:
        population = species.get("population", float('inf'))
        if population < lowest_population:
            lowest_population = population
            endangered_species = species.get("name", "")

    return endangered_species


# P2


# As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species. Each character in this string denotes a different endangered species. You also have a record of all observed species in a particular region, represented by the string observed_species. Each character in observed_species denotes a species observed in the region.

# Your task is to determine how many instances of the observed species are also considered endangered.

# Note: Species are case-sensitive, so "a" is considered a different species from "A".

# Write a function to count the number of endangered species observed.

# def count_endangered_species(endangered_species, observed_species):
#     pass
# Example Usage:

# endangered_species1 = "aA"
# observed_species1 = "aAAbbbb"

# endangered_species2 = "z"
# observed_species2 = "ZZ"

# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2))  
# Example Output:

# 3 # `a` and `A` are endangered species. `a` appears once, and `A` twice.
# 0

# SOLUTION
