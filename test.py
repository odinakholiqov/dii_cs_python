

numbers = [1,2,3,4]
even_numbers = []

def is_even(num):
    if num % 2 == 0:
        return True
    return False

for num in numbers:
    if is_even(num):
        even_numbers.append(num)

print(even_numbers)


print(
    list(
        filter(lambda x: x % 2 == 0, [_ for _ in range(11)])
    )
)

print(
    list(
        map(lambda x: x - 1, [1, 2, 3, 4])
    )
)

from functools import reduce
print(
    reduce(lambda x, y: x + y, [1, 2, 3, 4]) # type: ignore
)
