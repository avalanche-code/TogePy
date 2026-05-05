import requests

#USE RUFF as pylint         DONE, replaced pylint in uv/pyproject.toml
#USE HTTPX as requests

class APICaller:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon/"
        self.session1 = requests.session()

    def get_pokemon_name(self, name):
        #return self.session1.get(self.base_url + name).json()
        result = self.session1.get(self.base_url + name)
        if not result.ok: #if result.ok == False
            raise ValueError("Pokemon name not found")
        else:
            return result.json()
