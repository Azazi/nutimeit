from tests.StepDefinitions import StepDefinitions


class TestCacheStore(StepDefinitions):
    def setUp(self):
        from nutimeit._store.CacheStore import CacheStore
        self.store = CacheStore

    def tearDown(self):
        self.store.clear_results()
