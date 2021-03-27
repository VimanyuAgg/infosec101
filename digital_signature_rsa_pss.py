from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256


def sign(m, private_key):
    h = SHA256.new(m)
    signer = pss.new(RSA.importKey(private_key))
    return signer.sign(h)


def verify(m, s, public_key):
    h = SHA256.new(m)
    verifier = pss.new(RSA.importKey(public_key))
    try:
        verifier.verify(h, s)
        print('Signature is valid')
    except (TypeError, ValueError):
        print('Invalid Signature')


def run():
    m = b'crypto is awesome!'
    key = RSA.generate(2048)
    private_key = key.exportKey('PEM')
    public_key = key.publickey().exportKey('PEM')

    signature = sign(m, private_key)
    verify(m, signature, public_key)


if __name__ == '__main__':
    run()