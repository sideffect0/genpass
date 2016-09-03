from .utils import hash_codecs

def test_stdout():
    from backends import stdout
    for codec in hash_codecs:
        data = codec("genpass")
        stdout(data)          # expecting success
