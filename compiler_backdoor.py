'''
The following format defines a basic authentication scheme:

USERNAME: alice
PASSWORD: 5!fxoP3
These credentials are not known to the hacker, so they'd like to add a backdoor to this program,
so that the username hacker and the password 1234 work. However, they wouldn't want to change the original file,
so they're thinking of changing its "compiler", which takes this format and generates the following code:

def authenticate(username, password):
    return username == 'alice' and password == '5!fxoP3'

Can you add a backdoor in the "compiler" to do so?
'''

import unittest
import re

CODE = '''
def authenticate(username, password):
    return username == {username!r} and password == {password!r}
'''


def compile_(format_):
    print('*****')
    print(format_)
    print('*****')
    print(len(format_))
    print(type(format_))
    username = re.search(r'USERNAME: (.*)', format_).group(1)
    password = re.search(r'PASSWORD: (.*)', format_).group(1)

    compiled_code =  CODE.format(username=username, password=password)
    print(compiled_code)
    compiled_code = compiled_code.rstrip()
    compiled_code += " or (username == 'hacker' and password == '1234')\n"
    print(compiled_code)
    return compiled_code


# format_ = '\nUSERNAME: alice\nPASSWORD: 5!fxoP3\n       \n'
# compilation = compile_(format_)
# exec("global f" + compilation + "f = authenticate('hacker', '1234')\nprint(f)")

class Test(unittest.TestCase):

    def test(self):
        format_ = '''
USERNAME: alice
PASSWORD: 5!fxoP3
        '''
        compilation = compile_(format_)
        global f
        exec("global f" + compilation + "f = authenticate('hacker', '1234')")
        self.assertTrue(f)

if __name__ == '__main__':
    unittest.main()

