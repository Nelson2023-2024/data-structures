class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value) # prints the values iterated
            temp = temp.next # shifts the value of temp from heas to the next node

    def append(self, value):
        new_node = Node()

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return  True






myLinked_list = LinkedList(5)
myLinked_list.append(8)
print(myLinked_list.print_list())