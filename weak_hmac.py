# Implement the function weak-HMAC, which receives message and a 8-bytes (64-bit) long key,
# and returns its HMAC using SHA-1 with the given 8-byte (64-bit) ipad and opad.

import hashlib

ipad = b'123455678'
opad = b'abcdefghi'


def xor_two_bytes(a, b):
    l = [chr(a1^b1) for a1,b1 in zip(a,b)]
    return ''.join(l)


def weak_hmac(m, k, ipad, opad):
    print(m)
    print('*******')
    hash = hashlib.sha1()
    print(ipad)
    print(k)
    print(list(zip(ipad,k)))
    s_ipad = xor_two_bytes(ipad, k)
    s_opad = xor_two_bytes(opad, k)
    print(s_ipad + m)
    print(m)
    hash.update((s_ipad + m).encode('utf-8'))
    md1 = hash.hexdigest()
    print(md1)
    hash.update((s_opad + md1).encode('utf-8'))
    hmac = hash.hexdigest()
    return hmac


def run():
    m = 'hello world'
    k = b'crypto'
    print(weak_hmac(m,k,ipad, opad))


if __name__ == '__main__':
    run()
