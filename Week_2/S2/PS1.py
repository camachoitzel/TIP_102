"""
Imagine you are working on a wildlife conservation database. 
Write a function named most_endangered() that returns the species with the highest conservation priority based on its population.

The function should take in a list of dictionaries named species_list as a parameter. 
Each dictionary represents data associated with a species, including its name, habitat, and wild population. 
The function should return the name of the species with the lowest population.

If there are multiple species with the lowest population, return the species with the lowest index.

def most_endangered(species_list):
    pass
Example Usage:

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))
Example Output:

Vaquita


Undertsand:
Input- a list of dicts
Output- string of endangered species
Edge Cases- empty list, population not in dict

Plan:
create a int endangered var
create a string animal var 
iterate through each dict in list
check if population key exists
if it exists then check if it is less than the curr endagered var
return the name of the lowest population
"""

def most_endangered(species_list):
    most_endangered = float('inf')
    animal = ""

    for dict in species_list:
        
        if "population" not in dict:
            print("population missing from " + dict["name"])
         
     
        elif most_endangered > dict["population"]:
            most_endangered = dict["population"]
            animal = dict["name"]
            
    return animal

    


species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 50
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))


"""
As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species. Each character in this string denotes a different endangered species. You also have a record of all observed species in a particular region, represented by the string observed_species. Each character in observed_species denotes a species observed in the region.

Your task is to determine how many instances of the observed species are also considered endangered.

Note: Species are case-sensitive, so "a" is considered a different species from "A".

Write a function to count the number of endangered species observed.

def count_endangered_species(endangered_species, observed_species):
    pass
Example Usage:

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  
Example Output:

3 # `a` and `A` are endangered species. `a` appears once, and `A` twice.
0 
"""