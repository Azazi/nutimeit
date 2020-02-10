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
