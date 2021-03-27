# Implement the function encrypt, which receives a number and a public key and returns the encrypted number; and the
# function decrypt, which receives an encrypted number and the private key, and returns the original number.


def encrypt(m, public_key):
    e = public_key[1]
    n = public_key[0]
    return m**e % n


def decrypt(c, private_key):
    d = private_key[1]
    n = private_key[0]
    return c**d % n


def run():
    n = 33
    e = 7
    d = 3
    public_key = (n, e)
    private_key = (n, d)
    cipher = encrypt(30, public_key)
    message = decrypt(cipher, private_key)
    print(message == 30)


if __name__ == '__main__':
    run()
