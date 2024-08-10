# Question 2: Reverse a string

def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

print(reverse_string("hello"))  
print(reverse_string("A man a plan a canal Panama"))

