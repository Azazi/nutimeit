
from tests.StepDefinitions import StepDefinitions


class TestCallable(StepDefinitions):
    def test_update_count_once(self):
        callable = self.there_is_a_callable()

        callable.update_count()
        self.assertEqual(dict(callable)['count'], 1)

    def test_update_count_multiple(self):
        callable = self.there_is_a_callable()
        count = self.generate_random_int()

        for i in range(count):
            callable.update_count()

        self.assertEqual(dict(callable)['count'], count)

    def test_update_time_once(self):
        callable = self.there_is_a_callable()
        time = self.generate_random_int()

        callable.update_time(time)
        self.assertEqual(dict(callable)['time'], time)

    def test_update_time_multiple(self):
        callable = self.there_is_a_callable()
        count = self.generate_random_int()
        total_time = 0

        for i in range(count):
            time = self.generate_random_int()
            callable.update_time(time)
            total_time += time

        self.assertEqual(dict(callable)['time'], total_time)
