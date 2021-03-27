from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def encrypt(m, public_key):
    cipher = PKCS1_OAEP.new(RSA.importKey(public_key))
    return cipher.encrypt(m)


def decrypt(c, private_key):
    cipher = PKCS1_OAEP.new(RSA.importKey(private_key))
    return cipher.decrypt(c)


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