#main function

def prime(starting_range, ending_range):
    prime_storage = []
    flag = 0
    for increment1 in range(starting_range, ending_range):
        for increment2 in range(2, increment1):
            if (increment1%increment2 == 0):
                flag = 1
                break
            else:
                flag = 0
        if (flag == 0):
            prime_storage.append(increment1)
    return prime_storage

#driver

# starting_range = 0
# ending_range = 1000
# prime_storage = prime(starting_range, ending_range)
# print(prime_storage)
