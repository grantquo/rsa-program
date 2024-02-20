# main function

# def prime(starting_range, ending_range):
#     prime_storage = []
#     flag = 0
#     stopper = 0
#     increment1 = starting_range
#     while increment1 < ending_range and stopper == 0:
#         if len(prime_storage) < 10:
#             print(f"WHILE RUN: {increment1}")
#             for increment2 in range(2, increment1):
#                 if (increment1%increment2 == 0):
#                     flag = 1
#                     break
#                 else:
#                     flag = 0
#                 if (flag == 0):
#                     prime_storage.append(increment1)
#             increment1 += 1
#         else:
#             stopper = 1
#     return prime_storage

def prime(lower, upper):
    counter=0
    for num in range(lower, upper+1):
        if counter < 4:
            for i in range(3, num, 2):
                if (num%i)==0:
                    break
            else:
                print(num)
                counter += 1

prime(4294967296, 4300000000)
#driver

# starting_range = 4294967296 
# ending_range = 4500000000
# prime_storage = prime(starting_range, ending_range)
# print(prime_storage)
