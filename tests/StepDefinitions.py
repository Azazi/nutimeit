import random
import string
import unittest


class StepDefinitions(unittest.TestCase):
    def generate_random_string(self, length=10):
        return ''.join(
            [random.choice(string.ascii_lowercase) for x in range(length)]
        )

    def generate_random_int(self, low=2, high=5):
        return random.randint(low, high)
