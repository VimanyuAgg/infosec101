import random
import string


def generate_pswd(number_only):

    length = random.randint(4, 7)

    if number_only:
        print("ONLY NUMBERS ALLOWED IN SECRET")
        secret = random.choices(string.digits, k=length)
    else:
        print("ALL ASCII ALLOWED IN SECRET")
        secret = ''.join(random.choices(string.ascii_letters, k=length))

    print(f">>>Secret generated: {secret}<<<")
    return secret


