
def encrypt1(plaintext: str, k: int) -> str:
    """
    Basic implementation of caesar cipher
    """
    cipher = ''
    for p in plaintext:
        z = chr(((ord(p) - ord('a') + k) % 26) + ord('a'))
        cipher += z

    return cipher


def encrypt2(plaintext: str, k: int, alphabet: str = "abcdefghijklmnopqrstuvwxyz") -> str:
    """
    :param plaintext: non-encrypted plaintext
    :param k: shift in caesar cipher
    :param alphabet: alphabet string for the shift (this allows to change/expand the base text)
    :return: encrypted ciphertext
    """
    cipher = ''
    for p in plaintext:
        index_p = alphabet.find(p)
        if index_p != -1:
            cipher += alphabet[(index_p + k) % len(alphabet)]
        else:
            raise ValueError('non-alphabet found in plaintext')

    return cipher



