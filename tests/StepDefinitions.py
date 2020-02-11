import random
import string
import unittest


class StepDefinitions(unittest.TestCase):
    def generate_random_string(self, length=10):
        return ''.join(
            [random.choice(string.ascii_lowercase) for x in range(length)]
        )
