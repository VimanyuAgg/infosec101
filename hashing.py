import hashlib
import string
from itertools import combinations

def hash_md5(input):
    secure_hash = hashlib.md5()
    secure_hash.update(input.encode('utf-8'))
    return secure_hash.hexdigest()


def hash_sha1(input):
    secure_hash = hashlib.sha1()
    secure_hash.update(input.encode('utf-8'))
    return secure_hash.hexdigest()


def hash_sha256(input):
    secure_hash = hashlib.sha256()
    secure_hash.update(input.encode('utf-8'))
    return secure_hash.hexdigest()

def hash_sha3(input):
    secure_hash = hashlib.sha3_256()
    secure_hash.update(input.encode('utf-8'))
    return secure_hash.hexdigest()

def simple_hash(s):
    r = 7
    for letter in s:
        r *= 31
        r += ord(letter)
        r = int(r) % 2**16
    return r

def string_generator():
    for i in range(len(string.printable)):
        for j in combinations(string.printable, i+1):
            yield ''.join(j)


def find_collision_for_simple_hash(s):
    target = simple_hash(s)
    for candidate in string_generator():
        if (candidate != s) and (simple_hash(candidate) == target):
            return candidate

    return "this can never happen"


key_str = "Hello, world!"
print(hash_md5(key_str))
print(hash_sha1(key_str))
print(hash_sha256(key_str))
print(hash_sha3(key_str))
print(find_collision_for_simple_hash('foo'))