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

#Input Processsing
def block_splitter(text_input, block_num):
    block_list = []
    for character

def striplines(linelist):
    max = len(linelist)
    for iii in range(max):
        linelist[iii] = linelist[iii].strip()



def public_key(pqtext_input):
    #Grab inputs from line
    inputslist = pqtext_input.split()
    ppp = inputslist[0]
    qqq = inputslist[1]
    eee = inputslist[2]
    block = inputslist[3]
    modulus = ppp*qqq
    return ppp,qqq,eee,block,modulus

def private_key(p, q, e, modulus):
    modn = (p-1)*(q-1)
    d = (2*modn+1)/e
    return d

#Encryption/Decryption
def print_info():
    pass

def encrypt():
    pass

def decrypt():
    pass

def main():
    fpq = open("input1pq.txt","r")
    pqinputs = fpq.readlines()
    ftxt = open("input1text.txt", "r")
    txt = ftxt.readlines()
    striplines(pqinputs)
    striplines(txt)
    print(pqinputs)
    print(txt)



    fpq.close()
    ftxt.close()
    return
    

#Procedures


main()