from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random

def encrypt(m, public_key):
    hash = SHA.new(m)
    cipher = PKCS1_v1_5.new(RSA.importKey(public_key))
    ciphertext = cipher.encrypt(m+hash.digest())
    return ciphertext

def decrypt(c, private_key):
    dsize = SHA.digest_size
    sentinel = Random.new().read(15+dsize)  # Assume average data length is 15
    cipher = PKCS1_v1_5.new(RSA.importKey(private_key))
    m = cipher.decrypt(c, sentinel)
    digest = SHA.new(m[:-dsize]).digest()
    if digest == m[-dsize:]:
        print("Decryption is successful")
    else:
        print("Decryption is not successful")
    return m[:-dsize]


def run():
    key = RSA.generate(2048)
    private_key = key.exportKey('PEM')
    public_key = key.publickey().exportKey('PEM')
    c = encrypt(b'hello world', public_key)
    m = decrypt(c, private_key)
    print(m)
    print(m == b'hello world')


if __name__ == '__main__':
    run()
