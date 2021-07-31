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


def preserve_attr(source_func):
    """Decorator function that forwards source function attributes to wrapper.
    :param source_func: initial function that is being wrapped
    :type source_func: Callable
    :return: modified wrapper that preserves some source function attributes
    :rtype: Callable
    """
    def wrapper(wrapper_func):

        setattr(wrapper_func, "__name__", source_func.__name__)
        setattr(wrapper_func, "__doc__", source_func.__doc__)
        setattr(wrapper_func, "__original_func", source_func)
        return wrapper_func

    return wrapper


def print_result(func):
    @preserve_attr(func)
    def wrapper(*args, **kwargs):
        """Wrapper function that prints result of decorated function"""
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
