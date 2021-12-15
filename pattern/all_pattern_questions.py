"""
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4
"""
n = int(input())

for i in range(n) : 
    for j in range(1, n+1) : 
        print(j, end=" ")
    print()

"""
4 3 2 1 
4 3 2 1 
4 3 2 1 
4 3 2 1
"""
n = int(input())
for i in range(n) : 
    for j in reversed(range(1, n+1)) : 
        print(j, end=" ")
    print()


"""
1 2 3 
4 5 6 
7 8 9
"""
n = int(input())

count = 1 
for i in range(n) : 
    for j in range(n) : 
        print(count, end=" ")
        count += 1
    print()

"""
* 
* * 
* * * 
* * * *
"""

n = int(input())

for i in range(n) :
    for j in range(i+1) : 
        print('*', end=" ")
    print()

"""
1 
2 2 
3 3 3 
4 4 4 4
"""

n = int(input())

for i in range(n) : 
    for j in range(i+1) : 
        print(i+1, end=" ")
    print()

"""
1 
2 3 
4 5 6 
7 8 9 10
"""

n, count = int(input()), 1

for i in range(n) : 
    for j in range(i+1) : 
        print(count, end=" ")
        count += 1
    print()

"""
1 
1 2 
2 3 4 
4 5 6 7
"""

n, count = int(input()), 1

for i in range(n) : 
    for j in range(i+1) : 
        print(count, end=" ")
        count += 1
    count -= 1 
    print()

"""
1 
2 3 
3 4 5 
4 5 6 7
"""

n = int(input())

for i in range(n) :
    for j in range(i+1, 2*(i+1)) :
        print(j, end=" ")
    print()

"""
1 
2 1 
3 2 1 
4 3 2 1 
"""
# solution : 1
 
n = int(input())

for i in range(1,n+1) :
    for j in reversed(range(1,i+1)) :
        print(j, end = ' ')
    print() 

# solution : 2

n = int(input())

for i in range(1, n+1) : 
    for j in range(i) : 
        print(i-j, end=' ')
    print()

"""
A A A A 
B B B B 
C C C C
D D D D
"""

n = int(input())

#! ord('A') = 65
char = 65 
for row in range(n) :
    for col in range(n) : 
        print(chr(char), end=' ')
    char += 1
    print()

"""
A B C D
A B C D
A B C D
A B C D
"""

n = int(input()) 

for row in range(n) : 
    char = 65
    for col in range(n) : 
        print(chr(char), end=' ')
        char += 1 
    print()

"""
A B C D 
E F G H 
I J K L 
M N O P 
"""

n  = int(input())

char = 65
for row in range(n) : 
    for col in range(n) : 
        print(chr(char), end=' ')
        char += 1 
    print()

"""
A B C D 
C D E F 
E F G H 
G H I J 
"""

n = int(input())
char = 65
for row in range(n) : 
    for col in range(n) :
        print(chr(char), end = ' ')
        char += 1
    char -= 2 
    print()

"""
A 
B B 
C C C 
D D D D
"""

n = int(input())

char = 65 
for row in range(n) : 
    for col in range(row+1) : 
        print(chr(char), end= ' ')
    char += 1
    print()

"""
A 
B C 
D E F 
G H I J
"""

n = int(input())

char = 65 
for row in range(n) : 
    for col in range(row+1) : 
        print(chr(char), end=' ')
        char += 1 
    print()

"""
A 
B C 
C D E
D E F G
"""

n = int(input())

char = 65
for row in range(n) :
    counter = char 
    for col in range(row+1) : 
        print(chr(counter), end=' ')
        counter += 1 
    char += 1 
    print()

"""
D 
C D 
B C D 
A B C D 
"""

n = int(input())

char = 65 + n - 1

for row in range(n) : 
    counter = char 
    for col in range(row+1) : 
        print(chr(counter), end= ' ')
        counter += 1 
    char -= 1 
    print()

"""
A B C D
B C D E
C D E F 
D E F G 
"""

n = int(input())

char = 65 

for row in range(n) : 
    counter = char 
    for col in range(n) : 
        print(chr(counter), end=' ')
        counter += 1
    char += 1
    print()

"""
   *
  **
 ***
****
"""

n = int(input())
for row in range(1, n+1) : 
    print((n-row)*' ', end='')
    print(row*'*')

"""
****
***
**
*
"""

for row in reversed(range(1, int(input())+1)) : print(row*'*')

"""
****
 ***
  **
   *
"""

n = int(input())
for row in range(n) : 
    print((row)*' ', end='')
    print((n-row)*'*')

# or in one line 
n = int(input())
for row in range(n) : print((row)*' ', end=''); print((n-row)*'*')

"""
1111 
 222
  33
   4
"""
n = int(input())
for row in range(n) : print(row*' ', end= ''); print((n-row)*str(row+1))

"""
   1
  23 
 456
78910
"""

n = int(input())
counter = 1
for row in range(n) : 
    print((n-row)*' ', end= ''); 
    for j in range(row+1) : 
        print(counter, end='')
        counter += 1
    print()

"""
      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1
"""

n = int(input())

for i in range(n) : 
    for j in range(n-i-1) :  # 3 2 1
        print(' ', end=' ')
    for j in range(i+1) : 
        print(j+1, end=' ')
    for j in reversed(range(1,i+1)) : 
        print(j, end=' ')
    print()

"""
1 2 3 4 5 5 4 3 2 1 
1 2 3 4 * * 4 3 2 1 
1 2 3 * * * * 3 2 1 
1 2 * * * * * * 2 1
1 * * * * * * * * 1
"""

n = int(input())

for i in range(n) : 
    for j in range(n-i) :
        print(j+1, end = ' ')
    for j in range(i*2) : 
        print('*', end =' ')
    for j in reversed(range(n-i)) : 
        print(j+1, end=' ')
    print()