import random
import string


def generate_random_str(length):
    randomlst = [random.choice(string.ascii_letters+string.digits)
                 for i in range(length)]
    return ''.join(randomlst)
