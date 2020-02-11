from tests.StepDefinitions import StepDefinitions


class TestCacheStore(StepDefinitions):
    def setUp(self):
        from nutimeit._store.CacheStore import CacheStore
        self.store = CacheStore

    def tearDown(self):
        self.store.clear_results()

    def test_update_result_one_call(self):
        name, time = self.there_is_a_call_in_store()

        result = self.store.get_result(name)
        self.assertTrue(result)
        self.assertEqual(result['time'], time)
