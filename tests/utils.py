import hashes, backends
import inspect

hash_codecs = [func[1] for func in inspect.getmembers(hashes, inspect.isfunction)]
backends = [func[1] for func in inspect.getmembers(backends, inspect.isfunction)]
