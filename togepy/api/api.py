from os import name as os_name
from subprocess import call

import httpx

from togepy.models.pokemon import Pokemon


#single response principle
def clearconsole():
    call("cls" if os_name == "nt" else "clear")

class APICaller:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon/"
        self.session1 = httpx.Client()                          #Client() of httpx instead of requests' session()

    def get_pokemon_name(self, name) -> dict:
        result = self.session1.get(self.base_url + name)
        if result.is_error:
            raise ValueError("Pokemon name not found")
        else:
            #return json.loads(result.json()) doch falsch lol
            return result.json()


def sanitize_dict(api_reply: dict) -> dict:
    poke_dict = {"poke_id": None, "name": None, "maintype": None, "sectype": None}
    
    poke_dict["poke_id"] = api_reply["id"]
    poke_dict["name"] = api_reply["name"].title()
    poke_dict["maintype"] = api_reply["types"][0]["type"]["name"].title()

    if len(api_reply["types"]) > 1:
        poke_dict["sectype"] = api_reply["types"][1]["type"]["name"].title()
    else:
        poke_dict["sectype"] = None

    return poke_dict

def init_pokemon_obj(poke_dict: dict) -> Pokemon:
    pokemon = Pokemon(
        poke_dict["poke_id"],
        poke_dict["name"],
        poke_dict["maintype"],
        # poke_dict.get("sectype"))   #We know what to expect, so its ok, aber nicht gebraucht, ist immer da
        poke_dict["sectype"]
    )

    return pokemon

#maybe cache per pokemon and check if queried before and list of attacks/abilities exists
def change_ability(api_caller: APICaller, pokemon: Pokemon) -> list:
    reply = api_caller.get_pokemon_name(pokemon.name)
    poke_ability = reply["abilities"]
    abilities = []

    for ability in poke_ability:
        abilities.append(ability["ability"]["name"])

    return abilities

def change_moves(api_caller: APICaller, pokemon: Pokemon) -> list:
    reply = api_caller.get_pokemon_name(pokemon.name)
    poke_moves = reply["moves"]
    moves = []

    for move in poke_moves:
        moves.append(move["move"]["name"])

    return moves