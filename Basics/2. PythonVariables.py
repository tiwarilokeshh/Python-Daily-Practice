1. Given a double value d, typecast it to an integer value and print it.

d = float(input())
#code here
print(int(d))

2. Given an input num as a string. You need to typecast into an integer and double it. 

num = input()
#code here
number = int(num)
print(number * 2)

3. Given two numbers a and b, you need to swap their values so a holds the value of b and b holds the value of a. 
Just write the code to swap values of a and b at the specified place.

a = int(input())
b = int(input())
a, b = b, a
print(a, b)

4. Given an integer n find the sum of the first n natural number.

def nSum(n):
    #code here
    ans = 0
    
    for i in range(1, n+1):
        ans += i

    return ans



