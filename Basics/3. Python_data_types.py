1. You need to perform three separate tasks based on the given input:

String Input and Print: Read a text input as a string and print it as it is.
Integer Input and Add: Read an integer input n, add 10 to it, and print the result.
Float Input and Multiply: Read a floating-point number as input, multiply it by 10, and print the result.


s = str(input())
print(s)
# Take integer input and add 10 to the integer input and print
n = int(input())
print(n+10)
# Take floating-point input and multiply the float input by 10 and print
f = float(input())
print(f*10)


2. Given a tuple arr with distinct elements and an integer x, find the index position of x. Assume to have x in the tuple always. Print the index (0-based).

arr = tuple(map(int, input().split()))
x = int(input())

########### Write your code below ###############
# Print the index of x in arr
print (arr.index(x))


3. Given a decimal number n, return its binary equivalent.

class Solution:
    def decToBinary(self, n):
      return bin(n)[2:]


4. iven an input num as a string. You need to typecast into an integer and double it. 

num = input()
#code here
number = int(num)
print(number * 2)
