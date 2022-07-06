"""
arr vs linkedList 

to insert a value in some internal place in arr 
you have to swap millions of numbers depending on the size of the arr 
if the arr is full of capacity the whole arr will get copied to some other memory location

in linkedList you don't need to allocated a space. 
Singly Linked List -->  here you have a link to your next element in each element 
Doubly Linked List -->  here you have a link to your prev and next element in each element 
insertion is easier --> O(1) for element at the beginning 
at the end its O(n)
"""

class Node : 
    def __init__(self, data = None, next = None) : 
        self.data = data 
        self.next = next 

class linkedList : 
    def __init__(self) : 
        self.head = None

    def print_liked_list(self) : 
        if self.head is None : 
            print('Empty')
            return 
        
        itr = self.head 
        linkedList_str = ''
        while itr : 
            linkedList_str += str(itr.data) + '-->'
            itr = itr.next 

        print(linkedList_str)

    def insert_at_head(self, data) : 
        node = Node(data, self.head)
        self.head = node
         

    def insert_at_tail(self, data) : 
        if self.head is None :
            self.head = Node(data, None) 
            
        else : 
            itr = self.head 
            while itr.next : 
                itr = itr.next 

            itr.next = Node(data, None)

    def create_linked_list(self, data_list) : 
        self.head = None 
        for data in data_list : 
            self.insert_at_tail(data)

    def get_length(self) : 
        counter, itr = 0, self.head 
        while itr : 
            counter += 1 
            itr = itr.next
        return counter 

    def remove_at(self, index) : 
        if self.head is None : 
            print('empty')
        elif index == 0 : 
            self.head = self.head.next
        elif index >= self.get_length() : 
            print('index out of range')
        else : 
            itr, counter = self.head, 0
            while itr : 
                if counter+1 == index : 
                    if itr.next.next : 
                        itr.next = itr.next.next
                    else : 
                        itr.next = None 
                    break 
                itr = itr.next 
                counter += 1

    def insert_at(self, data, index) : 
        if index == 0 : 
            self.insert_at_head(data)
        elif index == self.get_length()-1 : 
            self.insert_at_tail(data)
        elif index >= self.get_length() : 
            print('index out of range')
        else : 
            itr, counter = self.head, 0
            while itr : 
                if counter+1 == index : 
                    itr.next = Node(data, itr.next)
                    break 
                itr = itr.next 
                counter += 1

    def insert_after_value(self, value, data) : 
        itr = self.head
        while itr : 
            if itr.data == value : 
                itr.next = Node(data, itr.next)
                break 
            itr = itr.next
            
        else : 
            print('value not present') 

    def remove_by_value(self, value) : 
        if self.head.data == value : 
            self.remove_at(0)
        else : 
            itr = self.head
            while itr.next : 
                if itr.next.data == value : 
                    itr.next = itr.next.next
                    break 
                itr = itr.next 
            else : 
                print('value not present') 

    def create_list(self) : 
        arr = []
        itr = self.head 
        while itr : 
            arr.append(itr.data)
            itr = itr.next 
        return arr  

    def reverse_linked_list(self) : 
        itr = self.head 
        prev = None 
        while itr : 
            next_node = itr.next 
            itr.next = prev 
            prev = itr 
            itr = next_node
        self.head = prev # else head is the 1st value 

        


if __name__ == '__main__' : 
    ll = linkedList() 
    ll.create_linked_list([2, 3, 4, 5, 6, 7, 8])
    print(ll.create_list())
    # ll.reverse_linked_list()
    # ll.insert_at(100, 4)
    # ll.insert_after_value(100, 99)
    # ll.print_liked_list()
    # ll.remove_by_value(99)
    # print(ll.get_length())
    # for i in range(ll.get_length()) : 
    #     ll.create_linked_list([2, 3, 4, 5, 6, 7, 8])
    #     ll.remove_at(i)
    #     ll.print_liked_list()
    # ll.insert_at_head(5)
    # ll.insert_at_head(6)
    # ll.insert_at_tail(7)
    # ll.print_liked_list()