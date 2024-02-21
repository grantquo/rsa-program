# D = 10958688116747337191
E = 1111111
P = 4294900427
Q = 4294901243
MODULUS = 18446173182483530761
PHIOFMODULUS = 18446173173893729092
import math

print(f"Modulus: {MODULUS} = {P*Q}")
print(f"Phi of Modulus: {PHIOFMODULUS} = {(P-1)*(Q-1)}")

m_int = 1371073485396775450
encrypted_int = pow(m_int, E, MODULUS)
print(10635173266219078295)
print(encrypted_int)
D = (1+(2*PHIOFMODULUS))/E
print(D)
# decrypted_int = pow(encrypted_int, int(D))%MODULUS
# print(1371073485396775450)
# print(decrypted_int)

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
