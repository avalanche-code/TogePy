class Pokemon:
    def __init__(self, pokedex_id: int,
                 name: str,
                 gender: str,
                 type: str,
                 ability:str,
                 moves: list[str] = None
                 ):
        #This to prevent "argument is mutable" warning if this is default value
        if moves is None:
            moves = ["/", "/", "/", "/"]
        else:
            self.moves = moves
        self.pokedex_id = pokedex_id
        self.name = name
        self.gender = gender
        self.type = type
        self.ability = ability

    def __add__(self, other):
        raise ValueError