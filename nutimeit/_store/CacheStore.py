from nutimeit._store.models.Callable import Callable


class CacheStore:
    """A class for interfacing with the cache storage.
    """
    _results = dict()

    @classmethod
    def get_results(cls):
        """Rettrieves all results from the cache store.

        Returns:
            (dict) -- A dictionairy representtation of all results in store
        """
        return {key: dict(cls._results[key]) for key in cls._results}

    @classmethod
    def get_result(cls, key):
        """Retrieves a specific Callable result from the cache store.

        Arguments:
            key (str) -- The name of the Callable

        Returns:
            (dict) -- A dictionaory representation of the Callable result.
        """
        return dict(cls._results.get(key, {}))

    @classmethod
    def update_result(cls, name, time):
        """Updates the aggregate monitoring stats for a Callable.

        Arguments:
            name (str) -- The name of the Callable
            time (float) -- Latest call running time in seconds
        """
        if name not in cls._results:
            cls._results[name] = Callable(name)

        cls._results[name].update_count()
        cls._results[name].update_time(time)
