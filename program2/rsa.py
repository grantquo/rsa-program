"""
/////////////////////////////////////////////////////////////////////
rsa.py
Main encryption/decryption file for RSA. Takes inputs for encryption
or decryption, processing them through RSA and outputting the result.
/////////////////////////////////////////////////////////////////////
"""
import sys
import os
import primegen

#Take Input
os.chdir("/home/kingkoobie/cs401/program2")
with open("input1text.txt","r") as f:
    startingtext = f.read()

#Present Input String
def get_input(txt):
    txt_char = ""
    data_list = txt.split()
    for iii in data_list:
        print(iii)
        int_iii = int(iii)
        txt_char += chr(int_iii)
    return print(txt_char)

def block_splitter(block_num):
    pass


#Encryption
def public_key(ppp, qqq, eee):
    pass

def private_key():
    pass

def encryption():
    pass

#Global RSA Vars
ppp = 0
qqq = 0
block_size = 0

def main():
    f = open("input1pq.txt","r")
    pqinputs = f.readline()




    getpq(pqinputs, ppp, qqq, block_size)
    print(f"ppp: {ppp}\nqqq: {qqq}\nblock_size: {block_size}")
    f.close()
    return
    

#Procedures


main()