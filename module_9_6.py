# Задача:
# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
#
# Пункты задачи:
# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
# Вызовите функцию all_variants и выполните итерации.


def all_variants(text):
    for i in range(1, len(text) + 1):
        for k in range(len(text)):
            if k + i > len(text):
                continue
            yield text[k:k + i]


# Пример работы функции:
a = all_variants("abc")
for i in a:
    print(i)
# Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc
#
# Примечания:
# Для функции генератора используйте оператор yield.