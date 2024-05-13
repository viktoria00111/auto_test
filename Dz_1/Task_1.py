"""
Задание 1.
Условие:
Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False
в противном случае. Передаваться должна только одна строка, разбиение вывода использовать не нужно.
"""

import subprocess


def func(command, text):
    res = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = res.stdout
    print(out)
    if res.returncode == 0:
        if text in out:
            return True
        else:
            return False
    else:
        print("FAIL! Code isn't 0")


if __name__ == "__main__":
    command_1 = "ls -la"
    text_1 = "dr"

    print(func(command_1, text_1))
