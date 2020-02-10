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
