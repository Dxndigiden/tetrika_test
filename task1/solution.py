import inspect
from functools import wraps


def strict(func):
    '''Проверяет типы аргументов согласно аннотациям'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        ann = func.__annotations__
        params = list(sig.parameters.keys())

        for arg_value, param_name in zip(args, params):
            expected_type = ann.get(param_name)
            if expected_type is None:
                continue

            if not isinstance(arg_value, expected_type):
                raise TypeError(
                    f'Аргумент {param_name} должен быть '
                    f'{expected_type.__name__}, '
                    f'а получен {type(arg_value).__name__}'
                )

        return func(*args, **kwargs)

    return wrapper
