import datetime

class Task:

    def __init__(self, content):
        self.content = content
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.content == other.content

    def __hash__(self):
        return hash(self.content)

    def __str__(self):
        return f'{self.content} (создано {self.time})'

todo_list = set()

todo_list.add(Task('Сделать домашку'))
todo_list.add(Task('Выпить кофе'))
todo_list.add(Task('Выйти на пробежку'))
todo_list.add(Task('Сделать домашку'))
todo_list.add(Task('Разобраться с магическими методами'))
todo_list.add(Task('Выпить кофе'))

for item in todo_list:
    print(item)

