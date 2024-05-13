""""
Задание 2. (повышенной сложности)
Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
в которомвывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из списка string.punctuation
модуля string). В этом режиме должно проверяться наличие слова в выводе.
"""

import subprocess
import re


def func(command, text, task=1):
    res = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = res.stdout

    print(out)
    if res.returncode == 0:
        if task == 1:
            print(out)
        elif task == 2:
            out = re.sub(r'[^\w\s]', ' ', out)
            print(out)
        else:
            print("Такого задания нет!")
            raise ValueError

        if text in out:
            return True
        else:
            return False
    else:
        print("FAIL! Code isn't 0")


if __name__ == "__main__":
    command_1 = "ls -la"
    text_1 = "dr"
    task_2 = 2

    print(func(command_1, text_1, task_2))
