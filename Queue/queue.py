class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_items(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def enqueue(self, value):
        new_node = Node(value)

        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node


        self.length += 1
        return True
    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        self.first = self.first.next
        temp.next = None
        return None


my_queue = Queue(4)
my_queue.enqueue(44)
my_queue.dequeue()
my_queue.print_items()