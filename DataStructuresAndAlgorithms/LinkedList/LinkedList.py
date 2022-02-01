

from logging import BufferingFormatter
from multiprocessing.sharedctypes import Value


class Node:
    def __init__(self, value):
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
        self.length += 1
    def pop(self):
        if self.length ==0:
            return None
        temp = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.head = new_node
    def Pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index , value):
        temp = self.get(value)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        temp.next = new_node
        self.length += 1
        return True
    def remove(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index == 0: 
            return self.Pop_first()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = self.tail
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



print('hello')

my_linked_list = LinkedList(19)

my_linked_list.append(11)
my_linked_list.append(15)
my_linked_list.append(20)
my_linked_list.prepend(41)

my_linked_list.insert(0,10)

my_linked_list.print_list()
print(my_linked_list.get(3).value , "get test")
print("hello")
print(my_linked_list.pop().value, "pop")

print(my_linked_list.head.value)
my_linked_list.reverse

my_linked_list.print_list()
    

