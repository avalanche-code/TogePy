class Pokemon:
    def __init__(self, pokedex_id: int,
                 name: str,
                 gender: str,
                 maintype: str,
                 sectype: str,
                 ability:str,
                 moves: list[str] = None
                 ):

        #This to prevent "argument is mutable" warning if this is default value, type already exists!
        if moves is None:
            moves = ["/", "/", "/", "/"]
        else:
            self.moves = moves

        self.pokedex_id = pokedex_id
        self.name = name
        self.gender = gender
        self.maintype = maintype
        self.sectype = sectype
        self.ability = ability

    def __add__(self, other):
        raise ValueError