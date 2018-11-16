class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def getNthNode(self,position):
        k = 1 
        temp = self.head # assigning temp node to traverse
        if position == 1:  # if position is 1st than return head node 
            return temp.data
        while(k<position and temp.next):
            k+=1
            temp = temp.next
        # print k     
        if position != k:  # if value of position is not equal to K than loop has iterated more than length of linked list
            print('Position Doesn\'t Exist')
            return ''
        return temp.data
if __name__=="__main__":
    llist = LinkedList() 
    llist.push(1) 
    llist.push(3) 
    llist.push(1) 
    llist.push(2) 
    llist.push(1) 
    print llist.getNthNode(int(input())) # Enter the node position here 
    
