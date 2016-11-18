import hashlib
import six

def hashlib_func(func):
    def do_hash(human_readable, service):
        hash = hashlib.new(func.__name__)
        hash.update(six.b(human_readable))
        return hash.hexdigest()
    return do_hash
