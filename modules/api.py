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

#single response principle