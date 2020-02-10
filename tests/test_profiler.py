import random
import unittest


class TestProfiler(unittest.TestCase):
    def setUp(self):
        from nutimeit.profiler import instrument
        from nutimeit._store import Store

        self.instrument = instrument
        self.store = Store

    def tearDown(self):
        self.store.clear_results()

    def test_instrument_one_call(self):
        @self.instrument
        def f():
            pass

        f()
        callable_name = '.'.join([__name__, 'f'])

        result = self.store.get_result(callable_name)
        self.assertTrue(result)

    def test_instrument_multiple_calls(self):
        @self.instrument
        def f():
            pass

        calls = random.randint(2, 5)
        callable_name = '.'.join([__name__, 'f'])
        for i in range(calls):
            f()

        result = self.store.get_result(callable_name)
        self.assertTrue(result)
        self.assertEqual(result['count'], calls)

    def test_instrument_no_calls(self):
        @self.instrument
        def f():
            pass

        callable_name = '.'.join([__name__, 'f'])
        result = self.store.get_result(callable_name)
        self.assertFalse(result)
