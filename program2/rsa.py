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
        if counter < block_num:
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
    inputslist = pqtext_input.split()
    ppp = int(inputslist[0])
    qqq = int(inputslist[1])
    eee = int(inputslist[2])
    block = int(inputslist[3])
    mod = int(ppp)*int(qqq)
    return ppp,qqq,eee,block,mod

def private_key(ppp, qqq, eee):
    phi_n = (ppp-1)*(qqq-1)
    ddd = (2*phi_n+1)//eee
    return ddd


#Output Processing
def ascii_convert(text_input):
    pass

def print_info():
    pass


#Encryption/Decryption
def encrypt(block_list, eee, nnn):
    encrypted_txt = ""
    for block in block_list:
        chars_list = block.split()
        encrypted_block = 0
        for character in chars_list:
            num = int(character)
            encrypted_block += (num**eee)% nnn 
        encrypted_txt += str(encrypted_block)+" "
    return encrypted_txt

def decrypt(ddd, encrypted_input):
    decrypted_blocks = []
    for block in encrypted_input:
        decrypted_block = 


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
    ppp, qqq, eee, block, modulus = public_key(pqinputs[0])
    txt_blocks = block_splitter(txt[0], block)
    
    ddd = private_key(ppp, qqq, eee)
    rsa_list = encrypt(txt_blocks, eee, modulus)
    plain_text_blocks = decrypt(ddd, rsa_list)



#Procedures


main()