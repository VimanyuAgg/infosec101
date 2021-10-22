'''
Implement the function sign so that given a line (in bytes), returns a unique signature of that line that is 20 characters long;
Implement the scan function that, given a list of paths and a signature, reads them line by line,
and returns a list of all the paths that have a line that matches the static signature.

Hints:
Any line in a file might end with a ‘\n’. Remember to remove it.
Don’t leave open files.
SHA1 is a good way to get a digest of a string.
'''

import hashlib


def sign(line):
    h = hashlib.sha1()
    h.update(line.rstrip())
    hash_val = h.hexdigest()[:20]
    print('for line: {}, hash: {}'.format(line, hash_val))
    return hash_val


def scan(paths, signature):
    matched_files = []
    for path in paths:
        print('reading path: {}'.format(path))
        print('signature: {}'.format(signature))
        with open(path) as f:
            for line in f:
                if sign(line.encode('utf-8')) == signature:
                    print('matched with signature: {}'.format(signature))
                    matched_files.append(path)

    return matched_files


known_virus_signature = '0beec7b5ea3f0fdbc95d'
filepaths_to_scan = ['./battleGrounds/file1_ns.txt', './battleGrounds/file2_s.txt', './battleGrounds/file3_s.txt']
infected_files = scan(filepaths_to_scan, known_virus_signature)

print(infected_files)