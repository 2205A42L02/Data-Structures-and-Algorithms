##print the length of the linkedlist
def sizeOfLL(self):
    size=0
    if(self.head):
        current_node=self.head
        while(current_node):
            size=size+1
            current_node=current_node.next
        return size
    else:
        return 0
    