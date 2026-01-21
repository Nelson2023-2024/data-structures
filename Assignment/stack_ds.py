from node import Node

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack_items(self):
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


    def pop(self):
        if self.top is None:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -=1
        return temp.value

    def pop_to_queue(self, queue):
        popped_node = self.pop()
        if popped_node is not None:
            queue.enqueue(popped_node)
            return popped_node
        return None






# my_stack = Stack(7)
#
# my_stack.push(4)
#
#
# my_stack.print_stack_items()