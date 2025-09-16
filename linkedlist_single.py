# What is LinkedList -: Linked list is a form of a sequential collection and it does not have to be in order.A Linkedlist is made up of independent nodes that may contain any type of data and each nodes has a reference to the next node in the link
# TYPES OF LINKED LIST -- - - (i)singly linked list (ii)circular singly linked list (iii)Doubly linked list (iv)circular Doubly linked list


# let's create at first node class constructor


class Node:  # class names are usually written in PascalCase
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:  # if the list is empty
            self.head = new_node
            self.tail = new_node
        else:  # otherwise, attach new_node at the end
            self.tail.next = new_node  # type: ignore
            self.tail = new_node
        self.length += 1


# testing
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)

print(new_linked_list.head.value)  # type: ignore # Output: 10
print(new_linked_list.head.next.value)  # type: ignore # Output: 20

# insertion in linked list in 3 way ---(i)at the beggining (ii)in the middle of linked list (iii)at the end of linked list
