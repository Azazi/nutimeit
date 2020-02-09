class Callable:
    """A class for storing monitoring stats of callables (i.e. methods &
    functions).

    Yields:
        name (str) -- name of Callable
        count (int) -- total count of calls to Callable
        time (float) -- total running time of all calls to Callable
    """
    def __init__(self, name):
        """Initializer method of a Callable.

        Arguments:
            name (str) -- Callable name argument
        """
        self._name = name
        self._count = 0
        self._time = 0

    def update_count(self):
        """Updates the total count of calls to the current Callable.
        """
        self._count += 1

    def update_time(self, call_time):
        """Updates the total running time of all calls to the current Callable.

        Arguments:
            call_time (float) -- Latest call running time in seconds
        """
        self._time += call_time

    def __iter__(self):
        """Generates an iterator from the Callable's properties

        Yields:
            name (str) -- name of Callable
            count (int) -- total count of calls to Callable
            time (float) -- total running time of all calls to Callable
        """
        yield 'name', self._name
        yield 'count', self._count
        yield 'time', self._time
