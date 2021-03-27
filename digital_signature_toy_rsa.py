def sign(m, private_key):
    return (m**private_key[1]) % private_key[0]


def verify(m, s, public_key):
    return m == (s**public_key[1]) % public_key[0]


def run():
    n = 33
    e = 7
    d = 3
    public_key = (n, e)
    private_key = (n, d)

    m = 29
    signature = sign(m, private_key)
    print(verify(m, signature, public_key))


if __name__ == '__main__':
    run()