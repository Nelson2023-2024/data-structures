"""

in append, prepend and insert we all have to create a new node so instead of crating at each point we just create the node class so that we can reference it once
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class LinkedList:
    def __init__(self, value):
        new_node = Node(value) # 1st node is created
        self.head = new_node # head and tail point to it
        self.tail = new_node
        self.length = 1

    # append item at the end of the linked list
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True


    def prepend(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length +=1
        return True

    # insert at a particular index
    def insert(self, value):
        pass
    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list = LinkedList(4)

my_linked_list.append(5)
my_linked_list.prepend(0)
print(my_linked_list.print_list())

# print(my_linked_list.tail.value)