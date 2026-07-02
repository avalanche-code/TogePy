from os import name as os_name
from subprocess import call

import httpx
import json
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
        if result.is_error:                                 #TODO: Check which error, errormsg corresponding to error
            raise ValueError("Pokemon name not found")
        else:
            return json.loads(result.json())


def query_pokemon(query_poke: str, apicaller: APICaller):   #TODO: default values where? code that instance is always default
    """This is a test function for querying pokemon, checking if API works. First attempt at unpacking"""
    pokemon1 = apicaller.get_pokemon_name(query_poke)

    ability_dictlist = []                                   #TODO: Better dictionary unpacking?
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



def sanitize_dict(api_reply: dict) -> dict:
    poke_dict = {"poke_id": None,
                 "name": None,
                 "maintype": None,
                 "sectype": None}
    poke_dict["poke_id"] = api_reply["id"]
    poke_dict["name"] = api_reply["name"]
    poke_dict["type"] = api_reply["types"][0]["type"]["name"]

    if len(api_reply["types"]) > 1:
        poke_dict["sectype"] = api_reply["types"][1]["type"]["name"]
    else:
        poke_dict["sectype"] = None

    return poke_dict
    #TODO: This function gets output of query, parses into dict thats easier to handle

def init_pokemon_obj(poke_dict: dict) -> Pokemon:
        pokemon = Pokemon(
            poke_dict["poke_id"],
            poke_dict["name"],
            poke_dict["maintype"],
            poke_dict.get("sectype"))

        return pokemon
    #TODO: This function get sanitized output, parses into new pokemon object