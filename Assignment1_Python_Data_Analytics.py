
# 1. Why dictionary keys must be immutable


print("Q1: Dictionary Keys Must Be Immutable")
my_dict = {"name": "Yogesh"}
print("Valid dictionary:", my_dict)





# 2. Frequency of elements in a list


print("\nQ2: Frequency of Elements")
elements = [1, 2, 2, 3, 4, 1, 2, 3]

frequency = {}

for item in elements:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Frequency dictionary:", frequency)



# 3. Difference between dict.get() and dict[key]


print("\nQ3: Difference between get() and []")
student = {"name": "Yogesh", "age": 20}

# Safe access using get()
print("Using get():", student.get("marks"))        
print("Using get() with default:", student.get("marks", 0))



# 4. Merge two dictionaries keeping larger value


print("\nQ4: Merge Dictionaries with Larger Value")

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 25, "c": 15, "d": 40}

merged = {}

for key in dict1:
    merged[key] = dict1[key]

for key in dict2:
    if key in merged:
        merged[key] = max(merged[key], dict2[key])
    else:
        merged[key] = dict2[key]

print("Merged dictionary:", merged)


# 5. Dictionary comprehension (odd numbers & cubes)


print("\nQ5: Dictionary Comprehension (Odd Cubes)")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

cube_dict = {num: num**3 for num in numbers if num % 2 != 0}

print("Odd cubes dictionary:", cube_dict)

