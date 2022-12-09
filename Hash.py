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
# todo_list.append(Task('Сделать домашку'))
# todo_list.append(Task(''))
# todo_list.append(Task('Сделать домашку'))
# todo_list.append(Task(''))
#
# non_empty_tasks = [item for item in todo_list if item]
# print(non_empty_tasks)
# len([item for item in todo_list if not item])

class TodoList():
    def __init__(self, start=0, stop = 2, step = 1):
        self.tasks = [None]*2  #Ничего умнее я не придумала с учетом того,
        #что в наших уроках ВООБЩЕ никак и нигде никто не объяснил, как делать вложенные классы,
        #а в гугле непонятно все.
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.tasks[self.value]
        else:
            raise StopIteration
    def __setitem__(self, key, value):
        self.tasks[key] = value

    # def __getitem__(self, item):
    #     return self.tasks[item]

    def __delitem__(self, key):
        del self.tasks[key]

    def __repr__(self):
        return str(self.tasks)


