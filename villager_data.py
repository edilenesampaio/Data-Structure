"""Functions to parse a file containing villager data."""

def all_species(filename):
    """Return a set of unique species in the given file.

    Return:
        - set[str]: a set of strings
    """
    
    unique_species = []
    file = open(filename)
    for line in file:
        species = line.rstrip().split("|")[1]
        unique_species.append(species)
        print()
    unique_species = set(unique_species)

        
    print(unique_species)
    file.close()      

    
    # unique_species = set([species])
    # unique_species = 
    # data = set(["villagers.csv"])

    return unique_species

 

# all_species("villagers.csv")

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    

    # TODO: replace this with your code

    villagers = []
    file = open(filename)

    for line in file:
        if search_string == "All":
            villagers.append(line.rstrip().split("|")[0])
        elif line.rstrip().split("|")[1] == search_string:
            villagers.append(line.rstrip().split("|")[0])
    file.close()
    print(sorted(villagers))
    return sorted(villagers)


# get_villagers_by_species("villagers.csv", "Anteater")



def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []
    names = []

    data = open(filename)
    for line in data:
        if line.rstrip().split("|")[3]== "Fitness":
            fitness = fitness.append(line.rstrip().split("|")[0])
        elif line.rstrip().split("|")[3]== "Nature":
            nature = nature.append(line.rstrip().split("|")[0])
        elif line.rstrip().split("|")[3]== "Education":
            education = education.append(line.rstrip().split("|")[0])
        elif line.rstrip().split("|")[3]== "Music":
            music = music.append(line.rstrip().split("|")[0])
        elif line.rstrip().split("|")[3]== "Fashion":
            fashion = fashion.append(line.rstrip().split("|")[0])
        elif line.rstrip().split("|")[3]== "Play":
            play = play.append(line.rstrip().split("|")[0])
        print("hello")
    data.close()

    names.append(fitness)
    print(names)
    # return []

all_names_by_hobby("villagers.csv")

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
