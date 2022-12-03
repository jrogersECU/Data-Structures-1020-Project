



class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

    def __str__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def length(self):
        count = 0
        if self.head == None:
            return count
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
            return count

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next







if __name__ == '__main__':

    llist = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    llist.append(node1)
    llist.append(node2)

    llist.printList()

