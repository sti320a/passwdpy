from unittest import TestCase
from passwdpy.core import generate_passwd


class TestCore(TestCase):

    def test_generate_passwd_length(self):
        len_passwd = len(generate_passwd(10))
        self.assertEqual(len_passwd, 10)
