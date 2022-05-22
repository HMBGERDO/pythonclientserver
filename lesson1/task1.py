# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих переменных. 
# Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.

task_group_words = ["разработка", "сокет", "декоратор"]

for word in task_group_words:
    print(f'{type(word)} \n {word} \n')

task_group_words_unicode = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', 
'\u0441\u043e\u043a\u0435\u0442', 
'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

for word in task_group_words_unicode:
    print(f'{type(word)} \n {word} \n')
