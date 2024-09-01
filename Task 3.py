smallest = 0
largest = 0
# smalllest = largest =0
user_input = input("Enter a number: ")
if user_input != "":
    number = float(user_input)
    smallest = largest = number

while user_input != "":
    number = float(user_input)

    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

    user_input = input("Enter another number: ")
print(largest)
print(smallest)
