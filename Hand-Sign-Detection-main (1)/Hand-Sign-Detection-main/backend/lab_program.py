#1st programm 1a
'''from datetime import datetime
name=input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth"))
current_year = datetime.now().year
age = current_year-year_of_birth
print("\n Name: ", name)
print("\n Age: ",age)
if age >= 60:
    print("Status: Senior citizen")
else:
    print("Status: Not a senior citizen")
#1b programm
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("\n Select Option")
print("1. Add")
print("2. Substract")
print("3.Multiply")
print("4. Divide")
choice = int(input("Enter your choice: "))
if choice == 1:
    result=a+b
    print("Result:",result)
elif choice == 2:
    result = a-b
    print("Result:",result)
elif choice == 3:
    result = a*b
    print("Result:",result)
elif choice == 4:
    if b != 0:
        result = a/b
        print("Result:",result)
    else:
        print("Dividing by zero not allowed")
else:
    print("Invalid choice")
#2a
N = int(input("Enter the value of N: "))
if N<=0:
    print("Please enter a positive integer")
else:
    fib_sequence = []
    a, b =0, 1
    for i in range(N):
        fib_sequence.append(a)
        a,b = b, a+b
    print("Fibonacci sequence of length",N,"is:")
    print(fib_sequence)
my_list = []
while True:
    print("\n ***List operation menu***")
    print(""" 1. Insert an element
              2.Remove an element
              3.append an element
              4.Display the length of the list
              5.Pop an element
              6.Clear the list
              7.Display the list
              8.Exit""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = input("Enter element to insert: ")
        position = int(input("Enter a position to insert at: "))
        my_list.insert(position, element)

        print("Element inserted successfully")
    elif choice == 2:
        element = input("Enter element to remove: ")
        if element in my_list:
            my_list.remove(element)
            print("Element removed successfully")
        else:
            print("Element not found")
    elif choice == 3:
         element = input("Enter element to append: ")
         my_list.append(element)
         print("Element appended successfully")
    elif choice == 4:
        print("Length of the list: ",len(my_list))
    elif choice == 5:
        if my_list:
            popped_element = my_list.pop()
            print("Popped element:",popped_element)
        else:
            print("List is empty.Nothing to pop")
    elif choice == 6:
        my_list.clear()
        print("List cleared successfully")
    elif choice == 7:
        print("Current list:",my_list)
    elif choice == 8:
        print("Exiting programm")
        break
#3a
import math
N = int(input("Enter the number of elements: "))
numbers = []
for i in range(N):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
mean = sum(numbers)/N
variance = sum((x-mean)**2 for x in numbers)/N
std_deviation = math.sqrt(variance)
print("\n Numbers:",numbers)
print("\n Mean:",mean)
print("\n Variance:",variance)
print("\n std deviation:",std_deviation)
#3b
number = input("Enter a multi digit number: ")
digit_count = {}
for digit in number:
    if digit.isdigit():
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
print(" \n Digit Frequency: ")
for digit in sorted(digit_count):
    print(f" Digit{digit} occurs {digit_count[digit]} time(S)")
#4
filename = input("Enter the file name: ")
with open(filename, 'r')as file:
    text = file.read()
words = text.lower().split()
cleaned_words = []
for word in words:
    word = word.strip(".,?:;\"'()[]{}")
    if word != " ":
        cleaned_words.append(word)
word_count={}
for word in cleaned_words:
    if word in word_count:
        word_count[word] = 1
    else:
        word_count[word] = 1
sorted_words = sorted(word_count.items(),
                      key=lambda x: x[1],
                      reverse = True)
print("/n Top 10 most frequently appearing words:\n")
for word,count in sorted_words[:10]:
    print(f"{word} : {count}")
#5
marks = []

print("Enter marks for 6 subjects:")

for i in range(6):
    mark = float(input(f"Enter mark {i+1}: "))
    marks.append(mark)

n = len(marks)

for i in range(n):
    for j in range(0, n-i-1):

        if marks[j] < marks[j+1]:

            marks[j], marks[j+1] = marks[j+1], marks[j]

print("\nMarks in descending order:")

for mark in marks:
    print(mark)
#6
input_file = input("Enter a input file name: ")
output_file = input("Enter a output file name: ")
with open(input_file, 'r') as file:
    lines = file.readlines()
cleaned_lines = []
for line in lines:
    line = line.strip()
    if len(line) > 0:
        cleaned_lines.append(line)

cleaned_lines.sort()
with open (output_file, 'w') as file:
    for line in cleaned_lines:
        file.write(line +"\n")
print("line sorted successfully")
print("sorted content written to:", output_file)
print("\nSorted Lines:")

for line in cleaned_lines:
    print(line)
def DivExp(a,b):
    assert a>0,"error,'a' must be greater than 0"
    if b==0:
        raise ValueError("Error:Division by zero is not allowed")
    c=a/b
    return c
try:
    a=float(input("Enter value for a: "))
    b=float(input("Enter value for b: "))
    result = DivExp(a,b)
    print(f"result of {a} / {b} = {result}")
except AssertionError as ae:
    print(ae)
except ValueError as ve:
    print(ve)
except Exception as e:
    print(e)
#8
class complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"
    def add_complex(c1,c2):
        return complex(c1.real+c2.real,c1.imag+c2.imag)
N = int(input("Enter the No of complex number(N>=2): "))
if N <2:
    print("N must be atleast 2")
else:
    complex_list = []
    for i in range(N):
        print(f"Enter complex number{i+1}: ")
        real = float(input("Real part: "))
        imag = float(input("Imag part: "))
        complex_list.append(complex(real,imag))
    total = complex_list[0]
    for i in range(1,N):
        total= complex.add_complex(total,complex_list[i])
    print("\n sum of all complex numbers: ",total)'''
#9
'''import string
def analyze_txt(text):
    translator = str.maketrans(" "," ",string.punctuation)
    cleaned_txt = text.translate(translator).lower()
    words = cleaned_txt.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    longest_word = max(words,key=len) if words else " "
    sentences = [s for s in text.replace('!','.').replace('?','.').split('.') if s.strip()]
    num_sentences = len(sentences)
    total_words = len(words)
    avg_word_len = sum(len(word) for word in words)/total_words if total_words>0 else 0
    print("\n ------Text analysis report------")
    print(f"total sentences: {num_sentences}")
    print(f" total words: {total_words}")
    print(f"longest word: {longest_word}")
    print(f"average word length: {avg_word_len}")
    print("\n Word frequencies: ")
    for word,freq in sorted(word_freq.items(),key = lambda x:x[1],reverse=True):
        print(f"{word}:{freq}")
paragraph = input("Enter a paragraph: ")
analyze_txt(paragraph)'''
#11
'''students = []
num_students = int(input("Enter number of students: "))
for i in range(num_students):
    name = input(f"Enter the name of student{i+1}: ")
    marks =int(input(f"Enter marks of {name}: "))
    students.append({'name':name,'marks':marks})
print("\n--------------- Student records-------")
for student in students:
    print(f"{student['name']}:{student['marks']}")
total_marks = sum(student['marks'] for student in students)
avg_marks = total_marks/num_students
print(f"Average marks:{avg_marks}")
topper = max(students,key=lambda x:x['marks'])
print(f"Topper = {topper['name']} with {topper['marks']} marks")
student_sorted = sorted(students,key=lambda x:x['marks'],reverse=True)
print("\n -----Student sorted marks------")
for student in student_sorted:
    print(f"{student['name']}:{student['marks']}")'''
'''it = ["apple","mango", "banana"]
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
    for char in fruit:
        print(char)

# Step 1: Define the paragraph
text = "learning python is fun and python is easy for learning"

# Step 2: Split the text into a list of words
words = text.split() 

# Step 3: Create an empty dictionary to store counts
word_count = {}

# Step 4: Loop through each word in the list
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1  # Increment count if word exists
    else:
        word_count[word] = 1                     # Add new word with count 1

# Step 5: Display the result
print("Word Frequencies:")
for k, v in word_count.items():
    print(f"{k} : {v}")
# 1. Creation
student = {'name': 'Rahul', 'branch': 'ISE', 'age': 19}

# 2. Lookup (Accessing a value)
print("Branch is:", student['branch'])  
# Output: Branch is: ISE

# 3. Insertion (Adding a new key-value pair)
student['college'] = 'Sir MVIT'
print("After Insertion:", student)
# Output: {'name': 'Rahul', 'branch': 'ISE', 'age': 19, 'college': 'Sir MVIT'}

# 4. Deletion (Removing a pair)
del student['age']
print("After Deletion:", student)
# Output: {'name': 'Rahul', 'branch': 'ISE', 'college': 'Sir MVIT'}
# Open a file in read mode
file = open("sample.txt", "r")

# Read the entire content into a string
content = file.read()

# Count characters (including spaces and newlines)
char_count = len(content)

# Count words (splitting the content by whitespace)
words = content.split()
word_count = len(words)

# Count lines (splitting by newline characters)
lines = content.split('\n')
line_count = len(lines)

# Close the file
file.close()

# Display results
print("Number of characters:", char_count)
print("Number of words:", word_count)
print("Number of lines:", line_count)
import numpy as np

# 1. Create a 3x3 array (a list of 3 lists)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Original 3x3 Array:")
print(matrix)

# 2. Display its shape (returns rows and columns)
print("\nShape of the array:", matrix.shape)

# 3. Display its transpose (swaps rows and columns)
print("\nTransposed Array:", matrix.T)
# .T is the shortcut for transpose
print("\n Mean of the matrix:",matrix.mean())
def test():
    x = 5
    print(x)

test()
a = [1,2,3]
b = a

b[0] = 100

print(a)
print(id(a))
print(id(b))'''
'''ss Time:
    pass

t = Time()

t.hour = 10
t.minute = 30
t.second = 15
print(Time)
import math          # Built-in scope contains the 'math' module

x = 10               # Global scope variable

def my_function():
    x = 5            # Local scope variable (takes precedence inside)
    print("Local x =", x)                 # Prints 5
    print("Built-in min =", min(20, 30))  # Using built-in 'min' function

my_function()
print("Global x =", x)                    # Prints 10
print("Qualified name =", math.pi)        # Using Dot Operator to access pi
class Point:
    # 1. Constructor / Initialization
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 2. String Representation
    def __str__(self):
        return f"({self.x}, {self.y})"

    # 3. Operator Overloading for '+'
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)  # Returns a new Point object

# --- Object Instantiation and Usage ---
p1 = Point(3, 4)
p2 = Point(1, 2)

print("Point 1 is:", p1)  # Triggers __str__ -> Prints: (3, 4)
print("Point 2 is:", p2)  # Triggers __str__ -> Prints: (1, 2)

p3 = p1 + p2              # Triggers __add__
print("Sum (p1 + p2):", p3)  # Prints: (4, 6)
def check_temperature(temp):
    if temp < -273:
        raise Exception("Temperature below absolute zero is impossible!")
    return f"Valid temperature: {temp}"

try:
    print(check_temperature(273))
except Exception as err:
    print("Error:", str(err))'''

import random

random.seed(10)

dice_roll = random.randrange(1, 7)
print("Dice roll integer:", dice_roll)

float_value = random.random()

print("Random float value:", float_value)

# Create two distinct lists with the same elements
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # list3 references the exact same object as list1

print("--- Comparing list1 and list2 ---")
# True because the values inside the lists are exactly the same
print(f"list1 == list2 is: {list1 == list2}") 
# False because they are stored in different memory locations
print(f"list1 is list2 is: {list1 is list2}") 

print("\n--- Comparing list1 and list3 ---")
# True because values are the same
print(f"list1 == list3 is: {list1 == list3}") 
# True because they point to the exact same object in memory
print(f"list1 is list3 is: {list1 is list3}")
import time
import random

print("Stopwatch Simulation Started...")

# Record the start time
start_time = time.time()

# Simulate a process taking a random amount of time (1 to 5 seconds)
delay = random.randint(1, 7)
print(f"Simulating a task that takes {delay} seconds...")
time.sleep(delay)

# Record the end time
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print(f"Stopwatch Stopped. Total time elapsed: {round(elapsed_time, 2)} seconds.")
# Using Python's built-in hash() function
key1 = "apple"
key2 = 100

# Generating hash values
hash_val1 = hash(key1)
hash_val2 = hash(key2)

print(f"The hash value of '{key1}' is: {hash_val1}")
print(f"The hash value of {key2} is: {hash_val2}")






     
    
        
      





          


