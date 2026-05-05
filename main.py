from utility import APICaller

my_apicaller = APICaller()
pokemon_name = input("Enter pokemon name: ")
ditto_raw = my_apicaller.get_pokemon_name(pokemon_name)
#if error isnt caught: aborts whole program!

#try:
#    ditto_raw = my_apicaller.get_pokemon_name(pokemon_name)
#except ValueError as e:
#    #print(f"{e}: Pokemon name is invalid")
#    raise ValueError("Pokemon name is not valid") from e

#if ditto_raw == 1:
#    print("Entered Pokemon name is invalid!")

ability_dictlist = []
for key, value in ditto_raw.items():
    if key == "abilities":
        #abilitylist.append(value) makes a list in a list
        ability_dictlist = value

#try printing abilitylist.items() to see how to address dict key value pairs?
#print(ability_dictlist) debugging to check how list looks

#hier direktzugriff statt 2 schleifen? z.b. nur eine schleife oder gar keine?
#nur eine schleife für k == "ability" und dann ability1 = v geht nicht, da neues dictionary, check structure
#hier noch eine schleifef for i in abilitylist:?
#alternative for pre-init variables with initially empty values of right type?

ability1 = ""
for k, v in ability_dictlist[0].items():
    if k == "ability":
        for k1, v2 in v.items():
            if k1 == "name":
                ability1 = v2

print(f"My first ability is {ability1}")

abilitylist = []

for item in ability_dictlist:
    for k, v in item.items():
        if k == "ability":
            for k1, k2 in v.items():
                if k1 == "name":
                    abilitylist.append(k2)

print(f"My abilities are {abilitylist}")