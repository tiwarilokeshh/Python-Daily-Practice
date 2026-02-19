1. ''' You are given two variables, a and b. Your task is to print these variables in the following formats:

With space: Print a and b in a single line, separated by a space, followed by a newline.
Without newline: Print a and b separated by a space, but do not end the output with a newline.
With separator: Print a and b separated by a specified separator, followed by a newline.
Without space: Print a and b in a single line, with no spaces between them, followed by a newline. '''

  
a = input()
b = input()
separator = input()[0]

########### Write your code below ###############

# Print with space
print(a, b)
# Print without newline at the end
print(a, b, end="")
# Print with separator
print(a, b, sep = separator)
# Print without space
print(a, b, sep="")

2. '''Given two inputs that are stored in variables a and n, you need to print a, n times 
      in a single line without space between them. Output must have a newline at the end.'''

a = input()
n = int(input())
print(a * n)

3. '''Given three inputs that are stored in the variables a, b, and c. You need to print a a times and b b times  in a single line separated by c.'''

a = int(input())
b = int(input())
c = input().strip()
# Write your code below that prints a a times and b b times, seperated by c
part1 = str(a) * a
part2 = str(b) * b

print(part1 + c + part2)


4. ''' You need to perform three separate tasks based on the given input:

String Input and Print: Read a text input as a string and print it as it is.
Integer Input and Add: Read an integer input n, add 10 to it, and print the result.
Float Input and Multiply: Read a floating-point number as input, multiply it by 10, and print the result. '''


# Take string input and print the string
s = input()
print(s)
# Take integer input and add 10 to the integer input and print
n = int(input())
print(n+10)
# Take floating-point input and multiply the float input by 10 and print
f = float(input())
print(f*10)

