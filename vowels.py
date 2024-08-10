# Question 1: Count Vowels

def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count

print(count_vowels("hello world"))        
print(count_vowels("The quick brown fox")) 
print(count_vowels("AEIOU")) 
print(count_vowels("Python Programming"))  
