# str | none fixes expected str, got none
class Pokemon:
    def __init__(self, pokedex_id: int,
                 name: str,
                 maintype: str,
                 sectype: str | None,
                 ):

        self.pokedex_id = pokedex_id
        self.name = name
        self.maintype = maintype
        self.sectype = sectype

        self.ability = ""
        self.moves = []   #ensure only 4 things

class PokeTeam:
    def __init__(self, team_name: str):
        self.team_name = team_name
        self.pokemons = []



        