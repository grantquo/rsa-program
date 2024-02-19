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
# with open("input1text.txt","r") as f:
#     startingtext = f.read()

# #Present Input String
# def get_input(txt):
#     txt_char = ""
#     data_list = txt.split()
#     for iii in data_list:
#         print(iii)
#         int_iii = int(iii)
#         txt_char += chr(int_iii)
#     return print(txt_char)

def block_splitter(block_num):
    pass


#Encryption
def public_key(ppp, qqq, eee):
    pass

def private_key(ppp, qqq, nnn):
    pass

def encryption():
    pass

def striplines(linelist):
    max = len(linelist)
    for iii in range(max):
        linelist[iii] = linelist[iii].strip()

def main():
    fpq = open("input1pq.txt","r")
    pqinputs = fpq.readlines()
    ftxt = open("input1text.txt", "r")
    txt = ftxt.readlines()
    striplines(pqinputs)
    striplines(txt)
    print(pqinputs)
    print(txt)



    # getpq(pqinputs, ppp, qqq, block_size)
    # print(f"ppp: {ppp}\nqqq: {qqq}\nblock_size: {block_size}")
    fpq.close()
    ftxt.close()
    return
    

#Procedures


main()