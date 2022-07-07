"""
Here we not only have the link to next node 
but also we have the link to prev node 
"""

class Node : 
    def __init__(self, data, next = None, prev = None) : 
        self.data = data 
        self.next = next 
        self.prev = prev 

class doublyLinkedList : 
    def __init__(self) : 
        self.head = None
        
    def insert_at_tail(self, data) : 
        if self.head is None : 
            self.insert_at_head(data)
        else : 
            itr = self.head 
            while itr.next : 
                itr = itr.next 

            itr.next = Node(data, None, itr) 

    def insert_at_head(self, data) : 
        if self.head is None : 
            self.head = Node(data, None, None) 
        else : 
            self.head = Node(data, self.head, None)

    def get_length(self) : 
        itr, counter = self.head, 0 
        while itr : 
            counter += 1 
            itr = itr.next 

        return counter 

    def insert_at(self, data, index) : 
        if index == 0 : 
            self.insert_at_head(data)
            
        elif index == self.get_length() - 1 : 
            self.insert_at_tail(data)

        elif index >= self.get_length() : 
            print('index out of range')

        else : 
            itr, counter = self.head, 0 
            while itr : 
                if counter+1 == index : 
                    itr.next = Node(data, itr.next, itr)
                    break 

                itr = itr.next 
                counter += 1 

    def create_linked_list(self, data_list) :
        self.head = None
        for data in data_list : 
            self.insert_at_tail(data) 

    def insert_after_value(self, value, data) : 
        itr = self.head 

        while itr : 
            if itr.data == value : 
                itr.next = Node(data, itr.next, itr)
                break 
            itr = itr.next 

        else : 
            print('value not found') 

    def remove_after_value(self, value) : 
        itr = self.head 
        while itr : 
            if itr.data == value : 
                itr.next = itr.next.next 
                break 
            itr = itr.next 
        else : 
            print('value not found')

    def remove_at(self, index) :
        if self.head is None : 
            print('empty')
        
        elif index >= self.get_length() : 
            print('index out of range')

        else : 
            itr, counter = self.head, 0
            while itr : 
                if counter+1 == index : 
                    itr.next = itr.next.next 
                    break 
                itr = itr.next 
                counter += 1

    def create_list(self) : 
        arr = []
        itr = self.head 
        while itr : 
            arr.append(itr.data)
            itr = itr.next

        return arr


    def print_doubly_linked_list(self) : 
        dll_string = '<-- '
        itr = self.head 

        while itr : 
            dll_string += str(itr.data) + ' <--> '
            itr = itr.next

        print(dll_string[:-6] + ' -->') 


if __name__ == '__main__' : 
    dll = doublyLinkedList()
    dll.create_linked_list([1, 2, 3, 4, 5, 6])
    dll.insert_at(100, 2)
    dll.remove_after_value(100)
    dll.insert_after_value(100, 99)
    print(dll.create_list())
    for i in range(dll.get_length()) :
        dll.create_linked_list([1, 2, 3, 4, 5, 6])
        dll.insert_at(100, i)
        dll.print_doubly_linked_list()
    dll.insert_at_head(1)
    dll.insert_at_head(2)
    dll.insert_at_head(3)
    dll.insert_at_head(4)
    dll.insert_at_tail(4)
    print(dll.get_length())
    dll.print_doubly_linked_list()