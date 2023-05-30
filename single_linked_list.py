class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node != None:
            length += 1
            current_node = current_node.next
        return length
    
    def append(self,data):
        next_node = Node(data=data)

        if self.head ==None:
            self.head = next_node
            self.tail = next_node
        else:
            self.tail.next = next_node
            self.tail = self.tail.next
    def delete_last(self):
        if self.head ==None:
            print("List is empty")
        else:
            if len(self) == 1:
                self.head = None
            else:
                current_node = self.head

                while current_node.next != None:
                    self.tail = current_node
                    current_node = current_node.next
                self.tail.next = None


    def insert(self,ID,data):
        new_node  = Node(data)
        if not 1<=ID<=len(self):
            print("Out of range")
        
        elif ID==1:
            new_node.next = self.head
            self.head = new_node
        else:
            cur_ID = 1
            cur_node = self.head
            while cur_ID+1 != ID:
                cur_node = cur_node.next
                cur_ID+=1
            new_node.next = cur_node.next
            cur_node.next = new_node
    
    def delete_index(self,ID):
        if self.head==None:
            print("List is empty")
        if ID==1 and len(self)>1:
            self.head = self.head.next
        elif 1<ID<len(self):
            cur_ID = 1
            cur_node = self.head
            while cur_ID!=ID:
                pre_node = cur_node
                cur_node = cur_node.next
                cur_ID+=1
            pre_node.next = cur_node.next
        elif ID == len(self):
            cur_ID = 1
            cur_node = self.head
            while cur_ID!=ID:
                pre_node = cur_node
                cur_node = cur_node.next
                cur_ID+=1
            pre_node.next = None
            self.tail = pre_node

        else:
            print("ID out of range")
    
    def reverse(self):
        pre_node = None
        cur_node = self.head
        self.tail = cur_node
        next_node = cur_node.next
        while next_node!=None:
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
            next_node = next_node.next 
        cur_node.next = pre_node
        self.head = cur_node
        return 
    def show_list(self):
        temp_list = self.head
        while temp_list!=None:
            print(temp_list.data)
            temp_list = temp_list.next
        
SL = SingleLinkedList()
SL.append(2)
SL.append(5)
SL.append(8)
SL.append(3)
SL.append(1)
SL.append(7)
SL.reverse()
print("====")
SL.insert(3,10)
SL.show_list()
SL.delete()
SL.show_list()

        
            
    


