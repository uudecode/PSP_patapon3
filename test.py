def func1(parameter1: float) -> None:
    """
    Очень полезная функция. котороая не возвращает ничего
    :param parameter1:
    :return:
    """
    print(parameter1)


def func2(parameter1: float) -> float:
    """
    Бла Бла квадрат вернем
    :param parameter1:  значение
    :return: возвращаем квадрат
    """
    return parameter1 * parameter1


print(type(print))
print(type(func1))
print(type(func2))

for i in range(0, 2000):
    func1(func2(float(i)))
