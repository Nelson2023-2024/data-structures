class Stack:
    def __init__(self):
        self.stack = []


    def push(self, value):
        return self.stack.append(value)
    def pop(self):
        return self.stack.pop()
    def print_items(self):
        for items in self.stack:
            print(items)

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []
    def stack_size(self):
        return len(self.stack)



my_stack = Stack()

my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
my_stack.push(7)


# my_stack.pop()
my_stack.print_items()


