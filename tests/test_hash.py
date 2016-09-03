import hashes
import inspect

hash_codecs = [func[1] for func in inspect.getmembers(hashes, inspect.isfunction)]

def test_all():
    for codec in hash_codecs:
        crypt = codec("genpass")
        assert crypt is not None
