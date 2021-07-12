"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func

print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий

До применения вашего декоратор будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция

Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""

import functools


def preserve_attr(func):
    """Decorator function that forwards wrapped function attributes to wrapper"""

    def wrapper(wrapped_func):

        setattr(wrapped_func, "__name__", func.__name__)
        setattr(wrapped_func, "__doc__", func.__doc__)
        setattr(wrapped_func, "__original_func", func)
        return wrapped_func

    return wrapper


def print_result(func):
    @preserve_attr(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add__"""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(f"Check that decorated function has original __doc__: {custom_sum.__doc__}")
    print(f"Check that decorated function has original __name__: {custom_sum.__name__}")
    without_print = custom_sum.__original_func
    print("Check that __original_func returns original function which prints nothing")
    # the result returns without printing
    without_print(1, 2, 3, 4)
