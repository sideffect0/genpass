import hashlib
import six

def hashlib_func(func):
    def do_hash(human_readable):
        hash = hashlib.new(func.__name__)
        hash.update(six.b(human_readable))
        return hash.hexdigest()
    return do_hash

@hashlib_func
def sha512():
    pass

@hashlib_func
def sha256():
    pass

@hashlib_func
def md5():
    pass

@hashlib_func
def sha1():
    pass

@hashlib_func
def sha224():
    pass

@hashlib_func
def sha384():
    pass
