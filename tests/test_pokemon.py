from togepy.api.api import APICaller, change_ability, change_moves
from togepy.main_old import query_pokemon_debug
from togepy.models.pokemon import Pokemon


def test_query_pokemon_debug():
    returnvalue = query_pokemon_debug("ditto")
    assert returnvalue == ["limber", ["limber", "imposter"]]

def test_change_ability():
    caller = APICaller()
    testpoke = Pokemon(1, "charizard", "", "")
    returnvalue = change_ability(caller, testpoke)
    assert returnvalue == ["blaze", "solar-power"]

def test_change_moves():
    caller = APICaller()
    testpoke = Pokemon(1, "ditto", "", "")
    returnvalue = change_moves(caller, testpoke)
    assert returnvalue == ["transform"]