from togepy.main_old import query_pokemon_debug


def test_query_pokemon_debug():
    returnvalue = query_pokemon_debug("ditto")
    assert returnvalue == ["limber", ["limber", "imposter"]]