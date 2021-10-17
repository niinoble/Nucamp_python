class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def iter_linked_list(node):
    while node is not None:
        print(node.value)
        node = node.next
        

class LinkedList:
    def __init__(self): 
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node is created: ", self.head.value)
            return
        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)
    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node is created: ", self.head.value)
            return
        new_node.next = self.head
        self.head = new_node
        print("Prepended new Head Node with value:",self.head.value)
        print("Node following Head is:" ,self.head.next.value)


llist = LinkedList()


llist.prepend("First Node")

