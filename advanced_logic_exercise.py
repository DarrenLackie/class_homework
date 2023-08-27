# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_integers = []

for number in numbers:
    if number % 2 == 0:
        even_integers.append(number)

print(even_integers)

# 2. Print the difference between the largest and smallest value:

largest_value = numbers[0]
smallest_value = numbers[0]

for number in numbers:
    if number > largest_value:
        largest_value = number
    if number < smallest_value:
        smallest_value = number
difference_between_values = largest_value - smallest_value

print(difference_between_values)

# 3. Print True if the list contains a 2 next to a 2 somewhere.

# print(range(len(numbers) - 1)) #prints range 0, 9. Allows you to check last index

for index in range(len(numbers) - 1):
        if numbers[index] == (numbers[index + 1]):
            same_numbers = True
            break
        else:
            same_numbers = False

print(same_numbers)


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

ignore_this_number = 6
restart_after_this_number = 7
sum_of_numbers = 0

for number in numbers:
    if number == ignore_this_number:
        continue
    if number == 7:
        break

sum_of_numbers += number

print(sum_of_numbers)
    # if number == start_again_after_this_number:
    #     number + 1 += sum_of_numbers






# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 







