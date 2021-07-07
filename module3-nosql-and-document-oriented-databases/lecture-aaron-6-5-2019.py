def recursive_sum(total, numbers):
    if not numbers:
        return total
    else:
        return recursive_sum(total + 
        numbers[0], numbers[1:])

numbers = list(range(1,11))

total = 0
print(numbers, total)

print(recursive_sum(total, numbers))