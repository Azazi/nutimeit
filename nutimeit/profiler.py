import time as _time
import inspect as _inspect

from nutimeit._store import Store as _Store


def instrument_module(m):
    """Profiles the execution time of all callables within a module.

    Arguments:
        m (module) -- The module to profile
    """
    _decorate_module(m)
    classes = _inspect.getmembers(m, _inspect.isclass)

    for klass in classes:
        _decorate_module(klass[1])


def instrument(f):
    """Profiles the execution time of a callable.

    Arguments:
        f (function) -- The callable to profile

    Returns:
        (any) -- The return value of the original callable
    """
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
    """Adds the instrument decorator to all callables within a module.

    Arguments:
        m (module) -- The module to profile.
    """
    functions = _inspect.getmembers(m, _inspect.isfunction)

    for function in functions:
        setattr(m, function[0], instrument(function[1]))
