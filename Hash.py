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

    def __repr__(self):
        return f'{self.content} (создано {self.time})'

    def __len__(self):
        return len(self.content)

# todo_list = set()
#
# todo_list.add(Task('Сделать домашку'))
# todo_list.add(Task('Выпить кофе'))
# todo_list.add(Task('Выйти на пробежку'))
# todo_list.add(Task('Сделать домашку'))
# todo_list.add(Task('Разобраться с магическими методами'))
# todo_list.add(Task('Выпить кофе'))
#
# for item in todo_list:
#     print(item)

todo_list = []
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))

non_empty_tasks = [item for item in todo_list if item]
print(non_empty_tasks)
len([item for item in todo_list if not item])