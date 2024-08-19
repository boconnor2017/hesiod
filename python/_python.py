# Python (v3) Template
# Author: Brendan O'Connor 
# Date: August 2023
#
# The purpose of this program is to provide enough of a starting point 
# to write python scrtipts without needing to do too much research
# on syntax. 

"""
This is a comment block
"""

# Send output to command line
a = "Hello world"
print(a)

# Print f-strings
agent_name = 'James Bond'
kill_count = 9
print(f'{agent_name} has killed {kill_count} enemies')


# Pass args to a python script
# Copy below into test.py
# From bash, run python3 test.py arg1 arg2
import sys
print(sys.argv[0]+" "+sys.argv[1]+" "+sys.argv[2])

# Prompt user for input
username = input("Enter username:")
print("Username is: " + username)

# Parse a string into an array 
mystring = "Something random separated by spaces"
myarray = mystring.split(" ")

# Loop through the array
i=0 
for x in array:
    print(x)
    i=i+1

# If then statement
x = 3
y = 10

if x < y:
    print("x is smaller than y.")
    
# Functions
boc1="HELLO!!!"
def boc_random(boc1):
 print("Starting boc_random")
 print("Passing value: "+boc1)

boc_random(boc1)

# Classes
class BOCClass1:
  x = 5
  y = 6
  z = 7

p1 = BOCClass1()
print(p1.x)
print(p1.y)
print(p1.z)

class BOCClass2:
  x = ["str1", "str2", "str3"]

p2 = BOCClass2()
print(p2.x[0])

# Calling APIs 
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.json())

# Pulling variables from other files
import vardata

print("Pulling data from var file...")
print("var1: "+vardata.var1)

# Reading a file
with open("readme.txt") as file:
    data = file.read()

print(data)

# Read a file and put each line into an array 
with open("readme.txt") as file:
    data = file.read()

i=0
line = data.split('\n')
for x in line:
    print("["+str(i)+"]"+line[i])
    i=i+1

# Append data to a list 
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

# Data Conversions
some_number = 5
some_string = str(some_number)

# Replace Method
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)