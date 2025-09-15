# What is LinkedList -: Linked list is a form of a sequential collection and it does not have to be in order.A Linkedlist is made up of independent nodes that may contain any type of data and each nodes has a reference to the next node in the link
# TYPES OF LINKED LIST -- - - (i)singly linked list (ii)circular singly linked list (iii)Doubly linked list (iv)circular Doubly linked list


# let's create at first node class constructor
class node:
    def __init__(self, value):
        self.value = value
        self.next = None


new_node = node(10)
print(new_node)
