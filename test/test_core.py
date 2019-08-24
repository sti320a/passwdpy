from unittest import TestCase
from passwdpy.core import generate_passwd


class TestCore(TestCase):

    def test_generate_passwd_length(self):
        len_passwd = len(generate_passwd(10))
        self.assertEqual(len_passwd, 10)

    def test_generate_passwd_complexity(self):
        import string
        target_passwd = generate_passwd(1)
        lower_cases = string.ascii_lowercase
        is_included_lowercase = True if set(
            list(target_passwd)
        ) & set(
            list(lower_cases)
        ) else False
        self.assertEqual(is_included_lowercase, True)


if __name__ == '__main__':
    test = TestCore()
    test.test_generate_passwd_complexity()
