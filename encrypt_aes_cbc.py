# Use PyCrypto to encrypt and decrypt with AES-CBC:
#
# Implement a function encrypt, that given a plaintext and a  16 -byte ( 128  bit) key  𝑘 ,
# picks a random  16 -byte ( 128  bit) IV, and returns a ciphertext encrypted with AES-CBC with the IV
# prepended to the ciphertext (in bytes).
#
# You may assume that the plaintext length (in bytes) is a multiple of 16.
#
# Implement a function decrypt, that given a ciphertext (as formatted by the encrypt function)
# and a  16 -byte ( 128  bit) key  𝑘 , returns the plaintext as decrypted by AES-CBC (in 'latin1').

from Crypto.Cipher import AES
from Crypto import Random
from collections import Counter

BLOCK_SIZE = 16


def xor_three(m1, m2, k):
    print(f"xoring: {m1} and {m2}")
    temp = xor(m1, m2)
    return xor(k, temp)


def xor(m1, m2):
    xord_val = ""
    for a, b in zip(m1, m2):
        xord_val += chr(ord(a) ^ ord(b))
    return xord_val


def my_aes_encrypt(plaintext, k):
    # On hindsight - this is not AES. this is just plain CBC
    iv = "asdfghjklzxcvbnm"
    ciphertext = iv
    prev_chunk = iv
    for i in range(0, len(plaintext), BLOCK_SIZE):
        encrypted_chunk = xor_three(prev_chunk, k.decode("utf8"), plaintext[i:i + BLOCK_SIZE].decode("utf8"))
        ciphertext += encrypted_chunk
        prev_chunk = encrypted_chunk

    return bytes(iv + ciphertext, encoding="latin1")  # return iv + ciphertext (in bytes)


def my_aes_decrypt(ciphertext, k):
    prev_chunk = ciphertext[:BLOCK_SIZE].decode("utf8")
    plaintext = ""
    ciphertext = ciphertext[BLOCK_SIZE:]
    for i in range(BLOCK_SIZE, len(ciphertext), BLOCK_SIZE):
        decrypted_chunk = xor_three(prev_chunk, k.decode("utf8"), ciphertext[i: BLOCK_SIZE + i].decode("utf8"))
        plaintext += decrypted_chunk
        prev_chunk = decrypted_chunk
    return bytes(plaintext, encoding='latin1')  # return plaintext (in 'latin1')


def aes_encrypt(plaintext, k):
    print(len(plaintext))
    deviation_from_block_size = len(plaintext) % AES.block_size
    print("padding needed: {}".format(deviation_from_block_size))
    plaintext = plaintext + bytes(' '*(AES.block_size - deviation_from_block_size), 'utf-8')
    print(len(plaintext))
    iv = Random.new().read(AES.block_size)  # Block size is 16
    return iv + AES.new(k, AES.MODE_CBC, iv).encrypt(plaintext)


def aes_decrypt(ciphertext, k):
    return AES.new(k, AES.MODE_CBC, ciphertext[:16]).decrypt(ciphertext[16:]).decode("latin1")


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def is_english(s):
    if not is_ascii(s) or not isinstance(s, str):
        return False

    word_frequency = Counter(s.lower())
    sorted_most_common_letters = list(sorted(word_frequency, key=word_frequency.get, reverse=True))
    top_three_letters = get_top_three_alphabets(sorted_most_common_letters)

    most_frequent_english_letters = set(['e', 't', 'a', 'o', 'i', 'n'])

    print(top_three_letters)
    return check_compatibility_in_english(top_three_letters, most_frequent_english_letters)


def get_top_three_alphabets(letters):
    top_three_letters = []

    counter = 0
    for letter in letters:
        if letter.isalpha():
            top_three_letters.append(letter)
            counter += 1

        if counter >= 3:
            return top_three_letters

    return []


def check_compatibility_in_english(list1, set1):
    if list1 is None or len(list1) == 0:
        return False

    return len(set(list1).intersection(set1)) > 0


def brute_force_aes(ciphertext):
    k1 = b'036'
    k2 = b'000000'
    k3 = b'0000000'
    for i in range(1000000):
        k = bytes(str(int(k2) + i).zfill(6), 'utf-8')
        candidate_key = k1 + k + k3
        print(f'Trying with key:{candidate_key}')
        candidate = aes_decrypt(ciphertext, candidate_key)
        print(f'Candidate with i:{i} - {candidate}')
        if is_english(candidate):
            print("**Looks like English!**")
            return candidate

    return "No Answer Found!"

k = b'0360056220000000'

# cipher = aes_encrypt(b'this is a normal english sentence', k)
# print("cipher: {}".format(cipher.decode('latin1')))
# decrypted_plaintext = brute_force_aes(cipher)
# print(f"C4ak3D: {decrypted_plaintext}")
# m = aes_decrypt(cipher, k)
# print(f"m: {m}")

r1="\x01\x04\x03\x09"  # dawn help
r2 = "\x14\x20\x03\x12"
c1="eetg"
c2="iaoy"
print(xor(c1, r2))
print(xor(c2,r2))

