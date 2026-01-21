from node import Node

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue_items(self):
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
            temp = self.last
            temp.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.length -= 1
        return temp.value

    def dequeue_to_stack(self, stack):
        dequeued_node = self.dequeue()
        if dequeued_node is not None:
            stack.push(dequeued_node)
            return dequeued_node
        return None




# my_queue = Queue(4)
#
# my_queue.enqueue(7)
# my_queue.enqueue(9)
# my_queue.dequeue()
# # print(my_queue.first.value)
# my_queue.print_queue_items()