import random
import string


def generate_random_str(length):
    randomlst = random.choices(string.ascii_letters+string.digits, k=length)
    return ''.join(randomlst)


if __name__ == '__main__':
    n = int(input())
    print(generate_random_str(n))
