from io import text_encoding


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_list(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height +=1
        return True

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        temp = None
        self.height -=1
        return temp






my_stack = Stack(3)


my_stack.push(44)
my_stack.push(45)
my_stack.push(46)
my_stack.pop()
# my_stack.pop()
my_stack.print_list()