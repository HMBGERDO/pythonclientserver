# 3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий
# сохранение данных в файле YAML-формата. Для этого:
# a. Подготовить данные для записи в виде словаря, в котором первому ключу
# соответствует список, второму — целое число, третьему — вложенный словарь, где
# значение каждого ключа — это целое число с юникод-символом, отсутствующим в
# кодировке ASCII (например, €);
# b. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а
# также установить возможность работы с юникодом: allow_unicode = True;
# c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они
# с исходными.

import yaml


data = {
    "first":[1, 2, 3],
    "second":4,
    "third":{
        "a":"123€",
        "b":"534213€",
        "c":"412€",
    },
}


def print_data_to_yaml(file, data):
    with open(file, "w", encoding="utf-8") as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

def read_data_from_yaml(file):
    with open(file, "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.SafeLoader)
    return data

if __name__ == "__main__":
    print_data_to_yaml('result.yaml', data)
    new_data = read_data_from_yaml('result.yaml')
    print(data == new_data)
