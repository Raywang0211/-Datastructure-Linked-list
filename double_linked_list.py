class Node:
    def __init__(self,data=None,next=None,pre=None):
        self.data = data
        self.next = next
        self.pre = pre

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def __len__(self):
        length = 0
        current_node = self.head
        while current_node != None:
            length += 1
            current_node = current_node.next
        return length

    def append(self,data):
        new_node = Node(data)

        if self.head ==None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next!=None:
                cur_node = cur_node.next
            new_node.next = cur_node.next
            cur_node.next = new_node
            new_node.pre = cur_node
    def delete_last(self):
        if self.head ==None:
            print("List is empty")
        else:
            if len(self)==1:
                self.head =None
            else:
                cur_node= self.head
                pre_node = cur_node.pre
                while cur_node.next!=None:
                    pre_node = cur_node
                    cur_node =cur_node.next
                pre_node.next = cur_node.next

    def delete_index(self,ID):
        if self.head ==None:
            print("List is empty")
        elif ID==1 and len(self)>1:
            self.head = self.head.next
        elif 1<ID<len(self):
            cur_node= self.head
            cur_ID = 0
            pre_node = cur_node.pre

            while cur_ID!=ID:
                pre_node = cur_node
                cur_node =cur_node.next
                cur_ID+=1
            pre_node.next = cur_node.next
            cur_node.pre = pre_node

        else:
            cur_node= self.head
            pre_node = cur_node.pre
            while cur_node.next!=None:
                pre_node = cur_node
                cur_node =cur_node.next
            pre_node.next = cur_node.next


    def insert(self,ID,data):
        new_node = Node(data)
        if self.head ==None:
            print("List is empty")
        elif ID==1 and len(self)>1:
            temp = self.head.next
            self.head = new_node
            self.head.next = temp
        else:
            cur_node= self.head
            cur_ID = 1
            pre_node = cur_node.pre

            while cur_ID!=ID:
                pre_node = cur_node
                cur_node =cur_node.next
                cur_ID+=1
            pre_node.next = cur_node.next
            cur_node.pre = pre_node

            pre_node.next = new_node
            new_node.pre = pre_node
            new_node.next = cur_node
            cur_node.pre =  new_node         

            
    def show_list(self):
        temp_node = self.head
        while temp_node!=None:
            print(temp_node.data)
            temp_node = temp_node.next

DL = DoubleLinkedList()
DL.append(1)
DL.append(10)
DL.append(2)
DL.append(9)
DL.show_list()
print("----")
DL.delete_index(4)
DL.show_list()
DL.insert(2,8)
print("---")
DL.show_list()
DL.insert(4,7)
print("---")
DL.show_list()


        