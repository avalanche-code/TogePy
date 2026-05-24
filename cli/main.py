from modules.helpers import (
    APICaller,
    clearconsole,
)


def __main__():
    clearconsole()
    # TODO: display error message here, check error flag!
    while True:
        print("What would you like to do?\n"
              "\t [1] Query Pokemon (testfunction)"
              "\t [2] View all Teams (not implemented yet)"
              "\t [3] Create new Team (not implemented yet)"
              "\t [4] View Details of Team (not implemented yet)\n\n")
        inp = input("Enter your choice (or press 'q' to quit): ")
        if inp == "q":
            return 0

        try:
            inp = int(inp)
            if inp < 1 or inp > 4:
                raise ValueError
        except ValueError:
            print("--------------------------------------------------\n"
                  "ERROR: Please enter a number between 1 and 4!\n"
                  "--------------------------------------------------\n")
            continue


my_apicaller = APICaller()
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