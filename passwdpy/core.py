import random
import string


def generate_passwd(length):
    randomstr = random.choices(string.ascii_letters+string.digits, k=length)
    return ''.join(randomstr)


if __name__ == '__main__':
    print(generate_passwd(int(input('Enter passwd length: '))))
