from __future__ import print_function

import argparse

import hashes, backends
from world import *

word_used = ""

def random_word():
    import random
    global word
    word = random.choice(words)  # need some awesome words 
    return word

if __name__== '__main__':
    parser = argparse.ArgumentParser(description="Genpass: Generates passwords to use in IRL")
    parser.add_argument("--hash", default="sha512", help="Algorithm to use for example: sha512, random")
    parser.add_argument("--backend", default="stdout", help="Saving backend to use for (default = stdout)")
    parser.add_argument("--data", default=random_word(), help="Human readable word (default = random word )")
    args = parser.parse_args()

    hash = getattr(hashes, args.hash)
    backend = getattr(backends, args.backend)

    password = hash(args.data)

    print("Using word : {}".format(word)) 
    print("crypt password generated : {}".format(password))
    print("Using Backend : {}".format(args.backend))
    backend(password)
