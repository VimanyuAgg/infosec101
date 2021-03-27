from Crypto.PublicKey import RSA

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')


def encrypt(m, public_key):
    # return ciphertext and key
    return RSA.importKey(public_key).encrypt(m, 32)


def decrypt(c, private_key):
    return RSA.importKey(private_key).decrypt(c)


m = 7
c = encrypt(m, public_key)
print(decrypt(c, private_key))