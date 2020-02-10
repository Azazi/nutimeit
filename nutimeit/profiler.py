import time as _time

from nutimeit._store import Store as _Store


def instrument(f):
    def timed(*args, **kw):
        ts = _time.time()
        result = f(*args, **kw)
        te = _time.time()

        _Store.update_result(
            name='.'.join([f.__module__, f.__name__]),
            time=te - ts
        )

        return result
    return timed


def _decorate_module(m):
    functions = _inspect.getmembers(m, _inspect.isfunction)

    for function in functions:
        setattr(m, function[0], instrument(function[1]))
