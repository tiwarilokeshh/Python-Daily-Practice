1. There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.

Now, complete the function which returns true if you are in trouble, else return false

def friends_in_trouble(j_angry, s_angry):
    return j_angry == s_angry


2.  Given a positive integer x. Your task is to check, if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number).


def checkOddEven(x):
    # code here
    if x%2 == 0:
        return "Even"
    else:
        return "Odd"


3. ou have to take an interger input a, and then use the if statement to print "Big" (without quotes) 
if the given number is greater than 100, and use the else statement to print "Small" (without quotes) when the number is smaller than or equal to 100.

def check_number(a):
    if a > 100:
        return "Big"
    else:
        return "Small"
        
a = int(input())
print(check_number(a))


4. Given a positive integer n, determine whether it is odd or even. Return true if the number is even and false if the number is odd.

class Solution:
    def isEven(self, n):
        if n % 2 == 0:
            return True
        else:
            return False


5. 





