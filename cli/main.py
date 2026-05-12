from modules.api import APICaller                   #folder structure: folder.module works, no / needed

my_apicaller = APICaller()
pokemon_name = input("Enter pokemon name: ")
pokemon1 = my_apicaller.get_pokemon_name(pokemon_name)

ability_dictlist = []
for key, value in pokemon1.items():
    if key == "abilities":
        ability_dictlist = value

#getting first ability
ability1 = ""
for k, v in ability_dictlist[0].items():
    if k == "ability":
        for k1, v2 in v.items():
            if k1 == "name":
                ability1 = v2

print(f"My first ability is {ability1}")

#getting all ability, maybe set stuff as active in pokemonclass later on, but keep everything?
#or json for all data, and then pokemonclass object for only current values? json for caching
#abilities are: 1: xyz, 2: abc, which do you want? type cli interface
#when called pokemon, make new object pokeclass, then filling from api calls, ablities etc?
abilitylist = []
for item in ability_dictlist:
    for k, v in item.items():
        if k == "ability":
            for k1, k2 in v.items():
                if k1 == "name":
                    abilitylist.append(k2)

print(f"My abilities are {abilitylist}")