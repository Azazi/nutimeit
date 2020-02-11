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

    def test_update_result_no_calls(self):
        results = self.store.get_results()
        self.assertFalse(results)

    def test_update_result_multiple_unique_calls(self):
        calls = dict()
        count = self.generate_random_int()

        for i in range(count):
            name, time = self.there_is_a_call_in_store()
            calls[name] = time

        for call in calls:
            result = self.store.get_result(call)
            self.assertTrue(result)
            self.assertEqual(result['time'], calls[call])

        results = self.store.get_results()
        self.assertTrue(results)
        self.assertEqual(len(results), count)

    def test_update_result_multiple_calls_same_function(self):
        name = self.generate_random_string()
        count = self.generate_random_int()
        total_time = 0

        for i in range(count):
            _, time = self.there_is_a_call_in_store(name=name)
            total_time += time

        result = self.store.get_result(name)
        self.assertTrue(result)
        self.assertEqual(result['time'], total_time)
        self.assertEqual(result['count'], count)

    def test_clear_results_empty(self):
        self.store.clear_results()

        results = self.store.get_results()
        self.assertFalse(results)

    def test_clear_results_not_empty(self):
        name, time = self.there_is_a_call_in_store()

        results = self.store.get_results()
        self.assertTrue(results)

        self.store.clear_results()
        results = self.store.get_results()
        self.assertFalse(results)
