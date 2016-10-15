#!/usr/bin/python 


class Node(object):
    
    def __init__(self,val,p = None):
        self.val = val 
        self.next = p
class LinkList(object):

    def __init__(self):
        self.head = None

    def initlist(self,data):
        self.head = Node(0)
        p = self.head
        
        for i in data:
            node = Node(i)
            p.next = node
            p = p.next
    def show(self):
        p = self.head.next
        while p != None:
            print p.val,
            p = p.next

    def getlength(self):
        p = self.head
        length = 0
        while p.next != None:

            length += 1
            p = p.next

        return length 
    def insert(self,index,val):
        if index < 0 or index > self.getlength():
            print "index is error"
            return
        p = self.head

        j = 0

        while p.next != None and j < index:
            p = p.next
            j += 1

        node = Node(val,p.next)
        p.next = node
    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

    def remove(self,index):
        if self.is_empty() or index < 0 or index > self.getlength():
            print "LinkList is empty or index error"
            return
        p = self.head
        j = 0
        while j < index and p != None:

            p = p.next
            j += 1
            
        p.next = p.next.next
    def replace(self,index,value):
        if self.is_empty() or index < 0 or index > self.getlength():
            print "LinkList is empty or index error"
            return 
        p = self.head.next

        i = 0

        while i < index:
            p =  p.next
            i += 1

        p.val = value
    def find(self,val):
        p = self.head.next
        while p != None:
            if p.val == val:
                return 1
            p = p.next

        return -1
l = LinkList()

l.initlist([1,2,3,4,5,6])

print l.getlength()

#l.insert(2,100)

#l.show()

#l.remove(3)
#l.show()

#l.replace(4,300)
#l.show()

print l.find(5)

