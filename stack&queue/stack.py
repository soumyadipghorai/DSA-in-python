"""
use --> store browser history 
LIFO --> last in first out 

push & pop -->O(1)
search element --> O(n)
"""

from collections import deque

stack = deque()

print(dir(stack)) # shows all the methods 

stack.append("https://link1.com")
stack.append("https://link2.com")
stack.append("https://link3.com")
stack.append("https://link4.com")

print(stack)

print(stack.pop()) # shows the last elements and drops it out of the list 

# stack class 
class Stack :

    def __init__(self) :
        self.container = deque()

    def push(self, data) : 
        self.container.append(data)

    def peek(self) :
        return self.container[-1]

    def pop(self) : 
        return self.container.pop()

    def is_empty(self) : 
        return len(self.container) == 0

    def size(self) : 
        return len(self.container)

def reverse_string(string) : 
    stack = Stack()
    for char in string : 
        stack.push(char)

    ans = ''
    while stack.size() != 0 : 
        ans += stack.pop()

    return ans 

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def balanced_paranthesis(string):
    stack = Stack()
    for ch in string:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0

if __name__ == '__main__' : 
    s = Stack()
    s.push(5)
    print(s.peek())
    print(s.pop())
    print(reverse_string("We will conquere COVI-19"))
    print(balanced_paranthesis("({a+b})"))
    print(balanced_paranthesis("))((a+b}{"))
    print(balanced_paranthesis("((a+b))"))
    print(balanced_paranthesis("((a+g))"))
    print(balanced_paranthesis("))"))
    print(balanced_paranthesis("[a+b]*(x+2y)*{gg+kk}"))