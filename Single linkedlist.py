class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    # Method to add a node at the beginning of the LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index (indexing starts from 0)
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if index == 0:
            self.insertAtBegin(data)
            return
        else:
            while current_node is not None and position + 1 != index:
                position += 1
                current_node = current_node.next
                
            if current_node is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")
    
    # Method to add a node at the end of the LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = new_node

    # Method to remove the first node
    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    # Method to remove the last node
    def remove_last_node(self):
        if self.head is None:
            return
        
        current_node = self.head
        if current_node.next is None:
            self.head = None
            return
        
        while current_node.next.next:
            current_node = current_node.next
            
        current_node.next = None

    # Method to remove a node at any index
    def remove_at_index(self, index):
        if self.head is None:
            return
        
        current_node = self.head
        position = 0
        if index == 0:
            self.remove_first_node()
            return
        else:
            while current_node is not None and position + 1 != index:
                position += 1
                current_node = current_node.next
                
            if current_node is not None and current_node.next is not None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
    
    # Method to print the size of the linked list
    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size
    
    # Method to print the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

# Create a new linked list
llist = LinkedList()

# Add nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

# Print the linked list
print("Node Data")
llist.printLL()

#