# Очередь
# В программировании существует потребность не только в изученных нами коллекциях. Одна из таких очередь. Она реализует подход к хранению данных по принципу «Первый вошёл – первый ушел».
#
# Реализуйте класс Queue, который не имеет параметров инициализации, но поддерживает методы:
#
# push(item) — добавить элемент в конец очереди;
# pop() — «вытащить» первый элемент из очереди;
# is_empty() — проверят очередь на пустоту.

class Stack:
    lst = []
    def push(self, item):
        self.item = item
        self.lst.append(self.item)


    def pop(self):
        return self.lst.pop()

    def is_empty(self):
        if len(self.lst) == 0:
            return True


stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")

