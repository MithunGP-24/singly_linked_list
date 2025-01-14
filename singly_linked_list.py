class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def inset_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_end(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def search(self,data):
        temp=self.start
        while temp  is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def print_item(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def delete_at_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_at_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.item is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                if temp.next.item==data:
                    temp.next=temp.next.next
                    break
                temp=temp.next



obj=SLL()
obj.inset_at_start(10)   
obj.inset_at_start(20)   
obj.inset_at_start(30)   
obj.inset_at_start(40) 
obj.insert_at_end(50)
obj.insert_after(obj.search(30),16)
obj.delete_at_first()
obj.delete_at_last()
obj.delete_item(20)
obj.print_item() 