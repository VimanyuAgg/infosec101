from Crypto.PublicKey import RSA
import Crypto.Hash.MD5 as MD5


def sign(m, private_key):
    h = MD5.new(m).digest()
    return RSA.importKey(private_key).sign(h, K='')


def verify(m, s, public_key):
    h = MD5.new(m).digest()
    assert RSA.importKey(public_key).verify(h, s)


def run():
    m = b'crypto is awesome!'
    key = RSA.generate(2048)
    private_key = key.exportKey('PEM')
    public_key = key.publickey().exportKey('PEM')

    signature = sign(m, private_key)
    verify(m, signature, public_key)


if __name__ == '__main__':
    run()