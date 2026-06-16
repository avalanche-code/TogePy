from modules.helpers import (
    APICaller,
    clearconsole,
)

# instancing object of api caller class. keeps connection open
my_apicaller = APICaller()


def main():

    clearconsole()
    SELECT_ERR = 0
    LIST_MIN = 1
    LIST_MAX = 4

    while True:
        # clearconsole() here.. think about how to keep results of funct showing before returning here
        # ("returning to menu") button
        if SELECT_ERR:
            print(
                "--------------------------------------------------\n"
                "ERROR: Please enter a number between 1 and 4!\n"
                "--------------------------------------------------\n"
            )
            SELECT_ERR = 0

        # Menu printing here
        print("What would you like to do?\n"
              "\t [1] Query Pokemon (testfunction)\n"
              "\t [2] View all Teams (not implemented yet)\n"
              "\t [3] Create new Team (not implemented yet)\n"
              "\t [4] View Details of Team (not implemented yet)\n\n")
        inp = input("Enter your choice (or press 'q' to quit): ")

        # check if user wants to quit with 'q'
        if inp == "q":
            return 0

        # check if input is in valid range: if not set flag "SELECT_ERR" = 1, raise error
        # theoretically I want to handle except at start of funct, so have to use flag?

        #continue statt try except
        try:
            inp = int(inp)
            if inp < LIST_MIN or inp > LIST_MAX:
                SELECT_ERR = 1
                raise ValueError
        except ValueError:
            continue

        match inp:
            case 1: query_pokemon()
            case 2: print("not yet implemented") #TODO
            case 3: print("not yet implemented") #TODO
            case 4: print("not yet implemented") #TODO


def query_pokemon():
    """This is a test function for querying pokemon, checking if API works. First attempt at unpacking"""
    pokemon_name = input("Enter pokemon name: ")
    pokemon1 = my_apicaller.get_pokemon_name(pokemon_name)

    ability_dictlist = []
    for key, value in pokemon1.items():
        if key == "abilities":
            ability_dictlist = value

    # getting first ability
    ability1 = ""
    for k, v in ability_dictlist[0].items():
        if k == "ability":
            for k1, v2 in v.items():
                if k1 == "name":
                    ability1 = v2

    print(f"My first ability is {ability1}")

    # getting all ability, maybe set stuff as active in pokemonclass later on, but keep everything?
    # or json for all data, and then pokemonclass object for only current values? json for caching
    # abilities are: 1: xyz, 2: abc, which do you want? type cli interface
    # when called pokemon, make new object pokeclass, then filling from api calls, ablities etc.?
    abilitylist = []
    for item in ability_dictlist:
        for k, v in item.items():
            if k == "ability":
                for k1, k2 in v.items():
                    if k1 == "name":
                        abilitylist.append(k2)

    print(f"My abilities are {abilitylist}")
    input("Press any key to continue...")

def query_pokemon_debug(querypokemon: str):
    """This is a test function for querying pokemon, checking if API works. First attempt at unpacking"""
    pokemon1 = my_apicaller.get_pokemon_name(querypokemon)

    ability_dictlist = []
    for key, value in pokemon1.items():
        if key == "abilities":
            ability_dictlist = value

    # getting first ability
    ability1 = ""
    for k, v in ability_dictlist[0].items():
        if k == "ability":
            for k1, v2 in v.items():
                if k1 == "name":
                    ability1 = v2

    # getting all ability, maybe set stuff as active in pokemonclass later on, but keep everything?
    # or json for all data, and then pokemonclass object for only current values? json for caching
    # abilities are: 1: xyz, 2: abc, which do you want? type cli interface
    # when called pokemon, make new object pokeclass, then filling from api calls, ablities etc.?
    abilitylist = []
    for item in ability_dictlist:
        for k, v in item.items():
            if k == "ability":
                for k1, k2 in v.items():
                    if k1 == "name":
                        abilitylist.append(k2)

    return [ability1, abilitylist]

if __name__ == "__main__":
    main()