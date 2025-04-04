a = []
b = input("Enter a list of numbers without commas: ")
numbers = list(map(int, b.split()))
a.extend(numbers)

print(a)
