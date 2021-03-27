from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


def sign(m, private_key):
    h = SHA256.new(m)
    return pkcs1_15.new(RSA.importKey(private_key)).sign(h)


def verify(m, s, public_key):
    h = SHA256.new(m)
    try:
        pkcs1_15.new(RSA.importKey(public_key)).verify(h, s)
        print('Signature is valid')
    except (TypeError, ValueError):
        print('Invalid signature')



def run():
    m = b'crypto is awesome!'
    key = RSA.generate(2048)
    private_key = key.exportKey('PEM')
    public_key = key.publickey().exportKey('PEM')

    signature = sign(m, private_key)
    verify(m, signature, public_key)


if __name__ == '__main__':
    run()