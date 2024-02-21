import math

# MODULUS = 91
# P = 7
# Q = 13
# PHIMOD = (P-1)*(Q-1)
# E = 5
# test_d = (1+(2*PHIMOD))/E
# print(test_d)
# message = 20
# print(message)
# message = pow(message, E, int(MODULUS))
# print(message)
# message = pow(message, int(test_d), int(MODULUS))
# print(message)

#message = 10469442895322594524
message = 4702394921427289856

p = 4294900427
q = 4294901243
phimod = (p-1)*(q-1)
n = p*q
e = 293
d = (1+(2*phimod))/e
print(f"D = {d}")
print(4702394921427289856)
print(message)
encrypted = pow(message, e, n)
print(encrypted)
decrypted = pow(encrypted, d)%n
print(4702394921427289856)
print(f"{decrypted} <- THIS SHOULD BE CORRECT~!")
