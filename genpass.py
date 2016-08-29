import hashlib
import six
import argparse

parser = argparse.ArgumentParser(description="Genpass: Generates passwords to use in IRL")
parser.add_argument("--algo", default="sha512", help="Algorithm to use for example: sha512, random")
parser.add_argument("--backend", default="stdout", help="Saving Backend to use for (default = stdout)")
args = parser.parse_args()
