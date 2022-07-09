"""
in flowing stock prices queue can be used 
in producer consumer problem its used 
    where producer produces the data in one end 
    and the consumer consumes the data in the other end 
FIFO --> first in first out    

access & search --> O(n)
insert delete --> O(1)
"""

wmt_stock_price_queue = []
wmt_stock_price_queue.insert(0, 131.10)
wmt_stock_price_queue.insert(0, 132.10)
wmt_stock_price_queue.insert(0, 131.50)
wmt_stock_price_queue.insert(0, 131.90)

# print(wmt_stock_price_queue)

# inserts the data at head and keep adding at head 
# during pop it pops the 1st element inserted 
# print(wmt_stock_price_queue.pop())
# print(wmt_stock_price_queue.pop())

from collections import deque

q = deque()

q.appendleft(5)
q.appendleft(6)
q.appendleft(7)
q.appendleft(8)
q.appendleft(5)

print(q.pop())

class Queue : 

    def __init__(self) :
        self.buffer = deque()

    def enqueue(self, data) : 
        self.buffer.appendleft(data)

    def dequeue(self) :
        return self.buffer.pop()

    def is_empty(self) : 
        return len(self.buffer) == 0 

    def size(self) : 
        return len(self.buffer)

if __name__ == '__main__' : 
    stock_queue = Queue()

    stock_queue.enqueue(
        {
            'company' : 'wmt', 
            'timestamp' : '15 apr, 11:01AM', 
            'price' : 131.1
        }
    )

    stock_queue.enqueue(
        {
            'company' : 'wmt', 
            'timestamp' : '15 apr, 11:02AM', 
            'price' : 131.2
        }
    )

    stock_queue.enqueue(
        {
            'company' : 'wmt', 
            'timestamp' : '15 apr, 11:03AM', 
            'price' : 133.1
        }
    )

    stock_queue.enqueue(
        {
            'company' : 'wmt', 
            'timestamp' : '15 apr, 11:04AM', 
            'price' : 132.1
        }
    )

    # print(stock_queue.buffer)
    print(stock_queue.dequeue())