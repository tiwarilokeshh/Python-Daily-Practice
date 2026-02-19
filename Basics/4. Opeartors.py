1. You are given two integer variables x and y. You need to perform the following operations:

p = x + y : Addition
q = x - y : Subtraction
r = x * y :Multiplication
s = x / y : Division
t = x % y : Modulo

x=int(input())
y=int(input())
#code here
# Perform addition x+y below
p = x+y
# Perform subtraction x-y below
q = x-y
# Perform multiplication x*y below
r = x*y
# Perform integer divison x//y below
s = x//y
# Perform modulo operation x%y below
t = x%y
print(p, q, r, s, t)

2.Logical operators and, or, not are used in condition checking. Like a and b checks if both a and b are True. First a is checked then b is checked. a or b checks if either of a or b is True. If one is True; it doesn't check for the other. not a complements the boolean value of a.
Note: 0 and empty string are False and all other values are True.
In this question you basically need to do
a and b
a or b
not a

a=int(input())
b=int(input())
#code here
p = a and b
#Do a or b below
q = a or b 
#Do not a below
r = not a 
#The code below prints the output. Don't change it!
print(p,q,r)


3. Given three positive integers a, b and c. Your task is to perform some bitwise operations on them as given below:
1. d = a ^ a
2. e = c ^ b
3. f = a & b
4. g = c | (a ^ a)
5. e = ~ e
Note: ^ is for xor.
Then print d e f g space seperately. Move the cursor to the next line after printing

a=int(input())
b=int(input())
c=int(input())
#code here
#Do a^a below
d= a ^ a
#Do c^b below
e= c ^ b
#Do a&b below
f= a & b
#Do c|(a^a) below
g= c|(a^a)
#Do ~e below
e=  ~e
print(d, e, f, g)


4.Given an integer N. FInd an integer K for which N%K is the largest ( 1 <= K < N).

Example 1:

Input:
N = 3
Output:
2
Explanation:
3%1 = 0
3%2 = 1
So, the modulo is highest for 2.

code : class Solution:
    def modTask(self, N):
        # code here
        N = int(input()).strip()
        print(N // 2 + 1)


5. Given an integer N. FInd an integer K for which N%K is the largest ( 1 <= K < N).

 

Example 1:

Input:
N = 3
Output:
2
Explanation:
3%1 = 0
3%2 = 1
So, the modulo is highest for 2


                         
class Solution:
    def modTask(self, N):
        # code here
        if N <= 0:
            return 0
        return N // 2 + 1

6. Given an integer n. Write a program to return the last digit of the number.

class Solution:
    def lastDigit(self, n: int) -> int:
        #Code here
        return abs(n) % 10

7. Given an integer n find the sum of the first n natural number.

  def nSum(n):
    #code here
    ans = 0
    
    for i in range(1, n+1):
        ans += i

    return ans


8. Given two integers a and b, You have to compute their LCM and GCD and return an array containing their LCM and GCD.

Examples:

Input: a = 5 , b = 10
Output: [10, 5]
Explanation: LCM of 5 and 10 is 10, while their GCD is 5.

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        x, y = a, b
        
        while y != 0:
            x, y = y, x%y
        gcd  = x
        
        lcm = (a * b) // gcd
        
        return [lcm , gcd]




