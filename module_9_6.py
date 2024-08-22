# Задача:
# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
#
# Пункты задачи:
# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
# Вызовите функцию all_variants и выполните итерации.


def all_variants(text):
    for l in text:
        yield l
    for k in range(len(text)):
        for j in range(k + 2, len(text) + 1):
            yield text[k:j]


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
