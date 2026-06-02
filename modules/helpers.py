from os import name as os_name
from subprocess import call

import httpx


class APICaller:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon/"
        self.session1 = httpx.Client()                          #Client() of httpx instead of requests' session()

    def get_pokemon_name(self, name):
        result = self.session1.get(self.base_url + name)
        if result.is_error:                                 #TODO: Check which error, errormsg corresponding to error
            raise ValueError("Pokemon name not found")
        else:
            return result.json()

def clearconsole():
    call("cls" if os_name == "nt" else "clear")
#single response principle