import hashlib
import six

hash = hashlib.new("sha512")
hash.update(six.b("sha512"))
