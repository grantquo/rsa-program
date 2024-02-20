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

def block_splitter(line_input, block_num):
    block_list = []
    counter = 0
    block_item = ""
    
    for element in line_input:
        if counter <= block_num:
            if element == " ":
                counter += 1
                block_item += element
            else:
                block_item += element
        else:
            block_list.append(block_item)
            block_item = element
            counter = 0
    
    if block_item != "":
        block_list.append(block_item)
    
    return block_list


def striplines(linelist):
    strippedlist = [iii.strip() for iii in linelist]
    return strippedlist

def public_key(pqtext_input):
    #Grab inputs from line
    print(pqtext_input)
    inputslist = pqtext_input.split()
    ppp = int(inputslist[0])
    qqq = int(inputslist[1])
    eee = int(inputslist[2])
    block = int(inputslist[3])
    modulus = int(ppp)*int(qqq)
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
    pqinputs = striplines(pqinputs)
    txt = striplines(txt)
    #Begin Key-Making
    block_splitter(txt[0], 7)

    ppp, qqq, eee, block, modulus = public_key(pqinputs[0])
#Procedures


main()