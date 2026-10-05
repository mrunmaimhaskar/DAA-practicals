NAME: MRUNMAI MANGESH MHASKAR
ROLL NO.: 41    	STUDENTID: 5593818
SUB: DATA STRUCTURE PRACTICALS






                         	PRACTICAL 1
1. Write a Program to Insert an Element in an Array.
Code:
arr = []
n =int(input("Enter number of elements: "))
for i in range(n):
 num=int(input("Enter element: "))
 arr.append(num)
print("Original Array:", arr)
position = int(input("Enter position to insert (1 to {}): ".format(n + 1)))
element = int(input("Enter element to insert: "))
arr.insert(position- 1, element)
print("Array after insertion:")
print(arr)
output:
Enter number of elements: 3
Enter element: 13
Enter element: 34
Enter element: 23
Original Array: [13, 34, 23]
Enter position to insert (1 to 4): 6
Enter element to insert: 12
Array after insertion:
[13, 34, 23, 12]






                                   
2. Write a Program to Access a Matrix Using Recursive Call.
CODE:
def display(matrix, rows, cols, i, j):
    if i == rows:
        return

    print(matrix[i][j], end=" ")

    if j == cols - 1:
        print()
        display(matrix, rows, cols, i + 1, 0)
    else:
        display(matrix, rows, cols, i, j + 1)


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

print("\nMatrix:")
display(matrix, rows, cols, 0, 0)

OUTPUT:
Enter number of rows: 3
Enter number of columns: 3
Enter matrix elements:
5
7
8
9
7
3
5
7
9

Matrix:
5 7 8 
9 7 3 
5 7 9 

#3. Program to Perform Addition and Multiplication of Two 2D Arrays.
CODE:
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

A = []
B = []

print("Enter elements of Matrix A")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A.append(row)

print("Enter elements of Matrix B")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    B.append(row)

print("\nAddition of Matrices")
for i in range(rows):
    for j in range(cols):
        print(A[i][j] + B[i][j], end=" ")
    print()

print("\nMultiplication of Matrices")
result = []

for i in range(rows):
    row = []
    for j in range(cols):
        total = 0
        for k in range(cols):
            total = total + A[i][k] * B[k][j]
        row.append(total)
    result.append(row)

for i in range(rows):
    for j in range(cols):
        print(result[i][j], end=" ")
    print()

OUTPUT:
Enter number of rows: 2
Enter number of columns: 2
Enter elements of Matrix A
5
9
7
4
Enter elements of Matrix B
3
6
5
8

Addition of Matrices
8 15 
12 12 

Multiplication of Matrices
60 102 
41 74 



4. Write a Program to Calculate the Transpose of a 2D Array.
CODE:
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements")

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

print("\nOriginal Matrix")

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()

print("\nTranspose Matrix")

for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()

OUTPUT:
Enter number of rows: 2
Enter number of columns: 2
Enter number of rows: 3
Enter number of columns: 3
Enter matrix elements
13
4
54
22
23
23
20
65
45

Original Matrix
13 4 54 
22 23 23 
20 65 45 

Transpose Matrix
13 22 20 
4 23 65 
54 23 45 




                                           PRACTICAL 2

1. Insert Element in Array. 
CODE:
arr=list(map(int,input("Enter elements: ").split()))
pos=int(input("Position: "))
val=int(input("Value: "))
arr.insert(pos-1,val)
print(arr)

OUTPUT:
Enter elements: 6
Position: 8
Value: 25
[6, 25]


2. Access Matrix Recursively 
CODE:
def show(a, i, j):
    if i == len(a):
        return

    print(a[i][j], end=" ")

    if j == len(a[0]) - 1:
        print()
        show(a, i + 1, 0)
    else:
        show(a, i, j + 1)


r, c = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(r)]

show(a, 0, 0)


OUTPUT:
2 3
1 2 3
4 5 6

1 2 3 
4 5 6 


3. Matrix Addition and Multiplication 
CODE:
r, c = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(r)]
B = [list(map(int, input().split())) for _ in range(r)]

print("Addition")

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    print(row)

print("Multiplication")

for i in range(r):
    row = []
    for j in range(c):
        s = 0
        for k in range(c):
            s += A[i][k] * B[k][j]
        row.append(s)
    print(row)

OUTPUT:
2 2
1 2
3 4
5 6
7 8
Addition
[6, 8]
[10, 12]
Multiplication
[19, 22]
[43, 50]


4. Transpose Matrix 
CODE:
r, c = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(r)]

for j in range(c):
    for i in range(r):
        print(a[i][j], end=" ")
    print()

OUTPUT:
3 5
1 4 6
2 5 4
2 6 4

1 2 2 
4 5 6 
6 4 4 


5. Stack Using List 
CODE:
# Stack
stack = []
stack.append(10)
stack.append(20)

print(stack)
print("Pop:", stack.pop())
print(stack)

# Linked List Insertion
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

temp = head

while temp:
    print(temp.data, end=" ")
    temp = temp.next

OUTPUT:
[10, 20]
Pop: 20
[10]
10 20 30 


















                                        PRACTICAL 3
Linear Search 
CODE:
a = list(map(int, input().split()))
key = int(input())

f = False

for i in range(len(a)):
    if a[i] == key:
        print("Found at", i)
        f = True
        break

if not f:
    print("Not Found")

OUTPUT:
10 30 50
10
Found at 0


Binary Search 
CODE:
a = sorted(list(map(int, input().split())))
key = int(input())

l = 0
r = len(a) - 1

while l <= r:
    m = (l + r) // 2

    if a[m] == key:
        print("Found")
        break
    elif key < a[m]:
        r = m - 1
    else:
        l = m + 1
else:
    print("Not Found")

OUTPUT:
10 20 30 40 50 
60
Not Found


Bubble Sort 
CODE:
a = list(map(int, input().split()))

for i in range(len(a)):
    for j in range(len(a) - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)

OUTPUT:
20 30 40 
[20, 30, 40]



Selection Sort 
CODE:
a = list(map(int, input().split()))

for i in range(len(a)):
    m = i

    for j in range(i + 1, len(a)):
        if a[j] < a[m]:
            m = j

    a[i], a[m] = a[m], a[i]

print(a)

OUTPUT:
20 50 60 30
[20, 30, 50, 60]


Insertion Sort 
CODE:
a = list(map(int, input().split()))

for i in range(1, len(a)):
    key = a[i]
    j = i - 1

    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
   a[j + 1] = key
print(a)
OUTPUT:
80 90 10 30 50
[10, 30, 50, 80, 90]





























                                         PRACTICAL 4
NumPy.
Write a Python program to create and display a NumPy array.
CODE:
import numpy as np
 
numbers = np.array([10, 20, 30, 40, 50])
 
print("Array:", numbers)

OUTPUT:
Array: [10 20 30 40 50]


Basic Operations on Array 
Write a Python program to perform addition, subtraction and multiplication on a NumPy array.
CODE:
import numpy as np
 numbers = np.array([10, 20, 30, 40, 50])
 
print("Original array:", numbers)
print("Addition:", numbers + 5)
print("Subtraction:", numbers - 5)
print("Multiplication:", numbers * 2) 

OUTPUT:
Original array: [10 20 30 40 50]
Addition: [15 25 35 45 55]
Subtraction: [ 5 15 25 35 45]
Multiplication: [ 20  40  60  80 100]



Find Maximum and Minimum 
Write a Python program to find the maximum and minimum value in a NumPy array. 
CODE:
import numpy as np
 
numbers = np.array([25, 10, 45, 30, 15])
 
print("Array:", numbers)
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

OUTPUT:
Array: [25 10 45 30 15]
Maximum: 45
Minimum: 10


Slice a NumPy Array 
Create a NumPy array containing 10 elements and display elements from the 1st to 5th position. 
CODE:
import numpy as np
 
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
 
print("Original array:", numbers)
 
print("First five elements:", numbers[0:5])

OUTPUT:
Original array: [ 10  20  30  40  50  60  70  80  90 100]
First five elements: [10 20 30 40 50]


Filter Array Values 
Write a Python program to display values greater than 50 from a NumPy array. 
CODE:
import numpy as np
 numbers = np.array([20, 45, 60, 75, 30, 90])
 
result = numbers[numbers > 50]
 
print("Values greater than 50:", result)

OUTPUT:
Values greater than 50: [60 75 90]

























                                          PRACTICAL 5
Pandas 
Create a Pandas DataFrame containing student names and marks. 
CODE:
import pandas as pd
 
data = {
	"Name": ["Rahul", "Priya", "Amit", "Sneha"],
	"Marks": [75, 85, 65, 90]
}
 
df = pd.DataFrame(data)
 
print(df) 

OUTPUT:
    Name  Marks
0  Rahul     75
1  Priya     85
2   Amit     65
3  Sneha     90






Display Statistical Information
Create a DataFrame of student marks and display statistical information. 
CODE:
import pandas as pd
 
data = {
	"Name": ["Rahul", "Priya", "Amit", "Sneha"],
	"Marks": [75, 85, 65, 90]
}
 
df = pd.DataFrame(data)
 
print(df)
print("\nStatistical Information:")
print(df["Marks"].describe())
 
OUTPUT:
    Name  Marks
0  Rahul     75
1  Priya     85
2   Amit     65
3  Sneha     90

Statistical Information:
count     4.000000
mean     78.750000
std      11.086779
min      65.000000
25%      72.500000
50%      80.000000
75%      86.250000
max      90.000000
Name: Marks, dtype: float64



Create Pandas Series from Dictionary
Create a Pandas Series using a dictionary containing student names and marks. 
CODE:
import pandas as pd
 
marks = {
	"Rahul": 75,
	"Priya": 85,
	"Amit": 65,
	"Sneha": 90
}
 
series = pd.Series(marks)
 print(series)

OUTPUT:
Rahul    75
Priya    85
Amit     65
Sneha    90
dtype: int64



Filter Pandas Series 
Create a Pandas Series of marks and display only marks greater than 70. 
CODE:
import pandas as pd
 
marks = pd.Series([55, 75, 80, 60, 90])
 
result = marks[marks > 70]
 
print("Marks greater than 70:")
print(result) 

OUTPUT:
Marks greater than 70:
1    75
2    80
4    90
dtype: int64





Simple Student Data Analysis
Create a DataFrame containing student names, marks and attendance. Display students who have marks greater than 70. 
CODE:
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Kiran"],
    "Marks": [75, 85, 60, 90, 65],
    "Attendance": [80, 90, 75, 95, 70]
}
df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nStudents scoring more than 70:")
print(df[df["Marks"] > 70])

OUTPUT:
Student Data:
    Name  Marks  Attendance
0  Rahul     75          80
1  Priya     85          90
2   Amit     60          75
3  Sneha     90          95
4  Kiran     65          70

Students scoring more than 70:
    Name  Marks  Attendance
0  Rahul     75          80
1  Priya     85          90
3  Sneha     90          95
                         
                         	 PRACTICAL 6
Write a Python program to create a linked list and display its elements.
CODE-:
class Node:
	def __init__(self, data):
    	self.data = data
    	self.next = None
 
# Create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
 
# Connect nodes
n1.next = n2
n2.next = n3
 
# Display linked list
current = n1
 
while current:
	print(current.data)
	current = current.next
	
output-:
10
20
30



2. Insert a new node at the beginning of a linked list.
code:
class Node:
	def __init__(self, data):
    	self.data = data
    	self.next = None
 
head = Node(20)
head.next = Node(30)
 
# Insert new node
new_node = Node(10)
new_node.next = head
head = new_node
 
# Display
current = head
 
while current:
	print(current.data)
	current = current.next
 
output-:
10
20
30
 

3.Insert a new node at the end of a linked list.
Code:
class Node:
	def __init__(self, data):
    	self.data = data
    	self.next = None
 
head = Node(10)
head.next = Node(20)
 
new_node = Node(30)
 
current = head
 
while current.next:
	current = current.next
 
current.next = new_node
 
current = head
 
while current:
	print(current.data)
	current = current.next
 
 output-:
10
20
30
 
 
 





5. Search an element in a linked list.
class Node:
	def __init__(self, data):
    	self.data = data
    	self.next = None
 
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
 
search = int(input("Enter value to search: "))
 
current = head
found = False
 
while current:
	if current.data == search:
    	found = True
    	break
	current = current.next
 
if found:
	print("Element found")
else:
	print("Element not found")
 
output-:
Enter value to search: 20
Element found
 
                            


                                   PRACTICAL 7  
1.Implement Stack Using List
CODE-:
stack = []
 
stack.append(10)
stack.append(20)
stack.append(30)
 
print("Stack:", stack)
 
print("Deleted:", stack.pop())
 
print("Stack after deletion:", stack)
 
output-:
Stack: [10, 20, 30]
Deleted: 30
Stack after deletion: [10, 20]
 
 

2.Implement Stack Using Menu.
CODE-:
stack = []
 
while True:
	print("\n1. Push")
	print("2. Pop")
	print("3. Display")
	print("4. Exit")
 
	choice = int(input("Enter choice: "))
 
	if choice == 1:
    	value = int(input("Enter value: "))
    	stack.append(value)
 
	elif choice == 2:
    	if len(stack) == 0:
        	print("Stack is empty")
    	else:
        	print("Deleted:", stack.pop())
 
	elif choice == 3:
    	print("Stack:", stack)
 
	elif choice == 4:
    	break
 
	else:
    	print("Invalid choice")
 
OUTPUT-:
1. Insert
2. Delete
3. Display
4. Exit
Enter choice: 1
Enter value: 10
 
1. Insert
2. Delete
3. Display
4. Exit
Enter choice: 1
Enter value: 20
 
1. Insert
2. Delete
3. Display
4. Exit
Enter choice: 3
Queue: [10, 20]
 
 
 
3. Implement a Circular Queue.
CODE-:
from collections import deque
 
queue = deque(maxlen=3)
 
queue.append(10)
queue.append(20)
queue.append(30)
 
print(queue)
 
queue.append(40
OUTPUT-:
deque([10, 20, 30])
deque([20, 30, 40])
 






4. Search for an element in a list using Linear Search.
CODE-:
numbers = [10, 20, 30, 40, 50, 60]
 
search = int(input("Enter number: "))
 
low = 0
high = len(numbers) - 1
 
while low <= high:
 
	mid = (low + high) // 2
 
	if numbers[mid] == search:
    	print("Element found")
    	break
 
	elif search > numbers[mid]:
    	low = mid + 1
 
	else:
    	high = mid - 1
 
else:
	print("Element not found")
OUTPUT-:
Enter number: 40
Element found
 




5. Sort a list using Bubble Sort.
CODE-:
numbers = [50, 20, 40, 10, 30]
 
for i in range(len(numbers)):
 
	for j in range(len(numbers) - i - 1):
 
    	if numbers[j] > numbers[j + 1]:
        	numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
 
print("Sorted list:", numbers)
 
OUTPUT-:
Sorted list: [10, 20, 30, 40, 50]
 
 
6. Sort a list using Selection Sort.
CODE-:
numbers = [50, 20, 40, 10, 30]
 
for i in range(len(numbers)):
 
	minimum = i
 
	for j in range(i + 1, len(numbers)):
 
    	if numbers[j] < numbers[minimum]:
        	minimum = j
 
	numbers[i], numbers[minimum] = \
    	numbers[minimum], numbers[i]
 
print(numbers) 
OUTPUT-:
[10, 20, 30, 40, 50]
 
 


7. Sort a list using Insertion Sort.
CODE-:
numbers = [50, 20, 40, 10, 30]
 
for i in range(1, len(numbers)):
 
	key = numbers[i]
	j = i - 1
 
	while j >= 0 and numbers[j] > key:
    	numbers[j + 1] = numbers[j]
    	j = j - 1
 
	numbers[j + 1] = key
 
print("Sorted list:", numbers)
OUTPUT-:
Sorted list: [10, 20, 30, 40, 50
                    






                               PRACTICAL 8
Implement Recursion – Factorial.
CODE-:
def factorial(n):
 
	if n == 0:
    	return 1
 
	return n * factorial(n - 1)
 
num = int(input("Enter number: "))
 
print("Factorial:", factorial(num))
OUTPUT-:
Enter number: 5
Factorial: 120
 
 
2.Create a Simple Binary Tree.
CODE-:
class Node:
 
	def __init__(self, data):
    	self.data = data
    	self.left = None
    	self.right = None
 
root = Node(10)
 
root.left = Node(20)
root.right = Node(30)
 
print("Root:", root.data)
print("Left:", root.left.data)
print("Right:", root.right.data)
 
OUTPUT-:
Root: 10
Left: 20
Right: 30
 
 
3. Perform Tree Traversal – Inorder.
class Node:
def __init__(self, data):
    	self.data = data
    	self.left = None
    	self.right = None
 
def inorder(root):
	
 
	if root:
 
    	inorder(root.left)
 
    	print(root.data)
 
    	inorder(root.right)
 
root = Node(10)
root.left = Node(20)
root.right = Node(30)
 
inorder(root)
OUTPUT-:
20
10
30
 
 
4. Implement Dictionaries as a Key-Value Data Structure.
CODE-:
student = {
	"RollNo": 101,
	"Name": "Rahul",
	"Marks": 85
}
 
print("Roll No:", student["RollNo"])
print("Name:", student["Name"])
print("Marks:", student["Marks"])
 
OUTPUT-:
Roll No: 101
Name: Rahul
Marks: 85
 

5.Count Frequency of Elements.
CODE-:
numbers = [10, 20, 10, 30, 20, 10]
 
frequency = {}
 
for number in numbers:
 
	if number in frequency:
    	frequency[number] += 1
	else:
    	frequency[number] = 1
 
print(frequency)
 
OUTPUT-:
{10: 3, 20: 2, 30: 1}
 

6. Find Word Frequency.
CODE
text = "python data science python data"
 
words = text.split()
 
frequency = {}
 
for word in words:
 
	if word in frequency:
    	frequency[word] += 1
	else:
    	frequency[word] = 1
 
print(frequency)
OUTPUT-:
{'python': 2, 'data': 2, 'science': 1}
 
 
7. Perform Set Operations.
Code:
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
 
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
 
OUTPUT-:
Union: {10, 20, 30, 40, 50, 60}
Intersection: {30, 40}
Difference: {10, 20}
 

8. Implement Stack Using Linked List.
Code:
class Node:
 
	def __init__(self, data):
    	self.data = data
    	self.next = None
 
stack = None
 
# Push 10
new_node = Node(10)
new_node.next = stack
stack = new_node
 
# Push 20
new_node = Node(20)
new_node.next = stack
stack = new_node
 
# Display
current = stack
 
while current:
	print(current.data)
	current = current.next
OUTPUT-:
20
10
 
 
9. Implement Queue Using Linked List.
from collections import deque
 
queue = deque()
 
queue.append(10)
queue.append(20)
queue.append(30)
 
print("Queue:", queue)
 
queue.popleft()
 
print("After deletion:", queue)

OUTPUT-:
Queue: deque([10, 20, 30])
After deletion: deque([20, 30])






