from togepy.api.api import (
    APICaller,
    change_ability,
    change_moves,
    init_pokemon_obj,
    sanitize_dict,
)
from togepy.models.pokemon import Pokemon


#Unit Test
def test_change_ability():
    #Arrange
    caller = APICaller()
    testpoke = Pokemon(1, "charizard", "", "")
    #Act
    returnvalue = change_ability(caller, testpoke)
    #Assert
    assert returnvalue == ["blaze", "solar-power"]

#Unit Test
def test_change_moves():
    caller = APICaller()
    testpoke = Pokemon(1, "ditto", "", "")
    returnvalue = change_moves(caller, testpoke)
    assert returnvalue == ["transform"]

#Unit Test
def test_sanitize_dict():
    caller = APICaller()
    data = caller.get_pokemon_name("ditto")
    returnvalue = sanitize_dict(data)
    assert returnvalue == {"poke_id": 132,
                           "name": "Ditto",
                           "maintype": "Normal",
                           "sectype": None}


#Integration Test
def test_init_pokemon_obj():
    miss_counter = 0

    caller = APICaller()
    data = caller.get_pokemon_name("ditto")
    testdict = sanitize_dict(data)
    returnvalue = init_pokemon_obj(testdict)
    targetpokemon = Pokemon(132, "Ditto", "Normal", None)
    if returnvalue.pokedex_id != targetpokemon.pokedex_id:
        miss_counter += 1
    if returnvalue.name != targetpokemon.name:
        miss_counter += 1
    if returnvalue.maintype != targetpokemon.maintype:
        miss_counter += 1
    if returnvalue.sectype != targetpokemon.sectype:
        miss_counter += 1

    assert miss_counter == 0