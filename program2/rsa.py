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

#Input Processsing
def block_splitter(text_input, block_num):
    block_list = []
    for character in text_input

def striplines(linelist):
    strippedlist = [iii.strip() for iii in linelist]
    return strippedlist

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


#Output Processing
def ascii_convert(text_input):
    pass

def print_info():
    pass


#Encryption/Decryption
def encrypt():
    pass

def decrypt():
    pass


#Main Processes
def main():
    
    #Input Files
    with open("input1pq.txt","r") as fpq:
        pqinputs = fpq.readlines()
    with open("input1text.txt", "r") as ftxt:
        txt = ftxt.readlines()
    
    striplines(pqinputs)
    striplines(txt)
    print(pqinputs)
    print(txt)

    #Begin Key-Making


    pass

#Procedures


main()