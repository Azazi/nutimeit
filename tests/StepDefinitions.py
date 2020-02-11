import random
import string
import unittest

from nutimeit._store.models import Callable


class StepDefinitions(unittest.TestCase):
    def generate_random_string(self, length=10):
        return ''.join(
            [random.choice(string.ascii_lowercase) for x in range(length)]
        )

    def generate_random_int(self, low=2, high=5):
        return random.randint(low, high)

    def there_is_a_call_in_store(self, name=None, time=None):
        _name = name or self.generate_random_string()
        _time = time or self.generate_random_int()

        self.store.update_result(_name, _time)
        return _name, _time

    def there_is_a_callable(self, name=None):
        _name = name or self.generate_random_string()
        return Callable(_name)
