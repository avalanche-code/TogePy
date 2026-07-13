from togepy.api.api import (
    APICaller,
    add_pokemon_to_team,
    change_ability,
    change_moves,
    init_pokemon_obj,
    sanitize_dict,
)
from togepy.models.pokemon import Pokemon, PokeTeam

#from togepy.tui.screens.query_menu import MAX_TEAM_SIZE macht coverage kaputt, liegt in screen
#test
MAX_TEAM_SIZE = 6

#All das wo api caller benutzt wird oder sonst was mit mock/dummy/stub/double?

#Unit Test
def test_poketeam_len():
    #Arrange
    team = PokeTeam("Team 1")
    testpoke = Pokemon(1, "ditto", "", "")
    #Act
    team = add_pokemon_to_team(team, testpoke)
    #Assert
    assert len(team.pokemons) == 1

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


#Unit Test
def test_poketeam_maxlen():
    team = PokeTeam("Team 1")
    testpoke = Pokemon(1, "ditto", "", "")
    for _ in range(0,10):
        team = add_pokemon_to_team(team, testpoke)
    assert len(team.pokemons) == MAX_TEAM_SIZE

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

#Mock
def test_change_ability_mock(mocker):
    #Mock von API Caller erstellen
    mock_api_caller = mocker.Mock()

    #Ergebnis von apicaller.get_pokemon_name mocken
    mock_result = {
        "id": 132,
        "name": "ditto",
        "types": [
            {
                "slot": 1,
                "type": {
                    "name": "normal",
                }
            }
        ],
        "abilities": [
            {
                "ability": {
                    "name": "transform"
                }
            }
        ]
    }

    #return wert der funktion auf unseren mock setzen
    mock_api_caller.get_pokemon_name.return_value = mock_result

    #zu testende funktion mit mock_api_caller aufrufen
    result = change_ability(mock_api_caller, Pokemon(1, "ditto", "", ""))
    assert result == ["transform"]

    #prüfen, ob die funktion genau ein mal aufgerufen wurde
    #Macht Mock zum Mock, und nicht zum Stub: Mock prüft zusätzlich Verhalten
    mock_api_caller.get_pokemon_name.assert_called_once_with("ditto")
