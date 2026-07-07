
class Pokemon:
    def __init__(self, pokedex_id: int,
                 name: str,
                 maintype: str,
                 sectype: str,
                 ):

        #This to prevent "argument is mutable" warning if this is default value, type already exists!
        self.pokedex_id = pokedex_id
        self.name = name
        self.maintype = maintype
        self.sectype = sectype

        self.ability = ""
        self.moves = ("/", "/", "/", "/")   #tuple nicht veränderbar, ist ass


    def __add__(self, other):
        raise ValueError

class PokeTeam:
    def __init__(self, team_name: str):
        self.team_name = team_name
        self.pokemons = []                  #List here or 6 pokemon objects