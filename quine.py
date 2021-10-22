s = 's = %r\nprint(s %% s)'
print(s % s)


def quine():
    hello = 'world'
    return "hello = 'world'\nreturn hello = 'world'"
