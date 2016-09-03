from .utils import hash_codecs

def test_rough():
    for codec in hash_codecs:
        crypt = codec("genpass")
        assert crypt is not None
        assert crypt != "genpass" # should not be
