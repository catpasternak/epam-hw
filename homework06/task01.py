"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(original_cls):
    """"""

    class Counter(original_cls):
        """Inherits from decorated class and adds counter logic.
        :param counter: class variable that counts number of class instances
        :type counter: int
        """

        counter = 0

        def __init__(self, *args, **kwargs):
            """Constructor method, inherits original class constructor method
            with any number of args and kwargs. Adds 1 to class variable `counter`.
            """
            super().__init__(*args, **kwargs)
            self.__class__.counter += 1

        @classmethod
        def get_created_instances(cls):
            """Returns number of created instances of the class.
            :return: value of `counter` variable
            :rtype: int
            """
            return cls.counter

        @classmethod
        def reset_instances_counter(cls):
            """Sets `counter` to zero.
            :return: number of class instances
            :rtype: int
            """
            result = cls.counter
            cls.counter = 0
            return result

    return Counter


@instances_counter
class User:
    pass


if __name__ == "__main__":

    print(f"{User.get_created_instances()=} (is it 0?)")  # 0
    user, _, _ = User(), User(), User()
    print("3 instances just created")
    print(f"{user.get_created_instances()=} (is it 3?)")  # 3
    print(f"{user.reset_instances_counter()=} (does it return 3?)")  # 3
    print(f"{user.get_created_instances()=} (is it 0 now?)")
