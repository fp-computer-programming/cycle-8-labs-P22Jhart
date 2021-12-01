def sum_to(num):

    total=0
    for value in range(int(num)+1):
        total += value
    return total

number = input("Give me a number")
print(sum_to(number))


