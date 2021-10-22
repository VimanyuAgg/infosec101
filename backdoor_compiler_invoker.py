# Don't change this:

import re
import unittest

CODE = '''
def authenticate(username, password):
    return username == {username!r} and password == {password!r}
'''

def compile_(format_):
    username = re.search(r'USERNAME: (.*)', format_).group(1)
    password = re.search(r'PASSWORD: (.*)', format_).group(1)
    return CODE.format(username=username, password=password)

# The rest you can change:

def run_compiler(format_):
    global CODE
    CODE = CODE.rstrip()
    CODE += " or (username == 'hacker' and password == '1234')\n"
    return compile_(format_)


class Test(unittest.TestCase):

    def test(self):
        format_ = '''
USERNAME: alice
PASSWORD: 5!fxoP3
        '''
        compilation = run_compiler(format_)
        global f
        exec("global f" + compilation + "f = authenticate('hacker', '1234')")
        self.assertTrue(f)


if __name__ == '__main__':
    unittest.main()