# Question 3: Filter even numbers

def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
    

print(filter_even_numbers([1, 2, 3, 4, 5]))
print(filter_even_numbers([10, 15, 20, 25])) 
print(filter_even_numbers([7, 11, 13])) 
print(filter_even_numbers([0, -2, -4]))  