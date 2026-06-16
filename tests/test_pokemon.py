from togepy.main import query_pokemon_debug as qpd


def test_qp():
    returnvalue = qpd("ditto")
    assert returnvalue == ["limber", ["limber", "imposter"]]