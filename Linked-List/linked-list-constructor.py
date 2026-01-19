# each linked list has a Node  -> value , next
# linked list -> head, tail, Node, length

class Node:
    def __init__(self, value, next =None): # the None accounts for the last element in the linked list which next is null
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return  True

    def pop(self):
        pre = self.head
        temp = self.head

        if self.head is None:
            return None

        # we stop the loop when ge get to the tail.next == None
        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -=1

        # in the case we have only one node so tail.next =None so the while loop doesnt run we remove the last element by making head and tail to None
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp, pre

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

    def pop_first(self):
        if self.head is None:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1

        #in the case we have only 1 item in thhe linked list so we set tail to None because head.next == None already
        if self.length == 0:
            self.tail = None

        return  temp # the item we removed from the linked list

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head # the 1st index

        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):

        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0 :
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index -1 )
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp


    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after








my_linked_list = LinkedList(4)

my_linked_list.append(99)
my_linked_list.append(200)
# my_linked_list.pop()
my_linked_list.prepend(23)
my_linked_list.pop_first()
my_linked_list.set_value(1, 45)

my_linked_list.reverse()

my_linked_list.print_list()

# print(my_linked_list.get(2).value)
# print(type(my_linked_list))
# print(my_linked_list.head.value)