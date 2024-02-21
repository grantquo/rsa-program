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

def block_encoder(line_input, block_size):
    block_list = []
    counter = block_size-1
    block_item = 0
    line_vals = line_input.split()

    for iii in line_vals:
        iii = int(iii)
        encoded_iii = iii*256**counter
        if counter > 0: #if block size hasnt been reached
            counter -= 1
            block_item += encoded_iii
        else: #if block size has been reached
            counter = block_size-1
            block_list.append(block_item)
            block_item = encoded_iii

    if block_item > 0:  #if partial block is made
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
    ddd = (1*phi_n+1)/eee
    return ddd,phi_n


#Output Processing
def ascii_convert(text_input):
    pass

def print_info():
    pass


#Encryption/Decryption    

def encrypt(block_list, eee, modulus):
    encrypted_blocks = []
    for block in block_list:
        encrypted_blocks.append((block**eee) % modulus)
    return encrypted_blocks
    # encrypted_txt = ""
    # for block in block_list:
    #     chars_list = block.split()
    #     encrypted_block = 0
    #     for character in chars_list:
    #         num = int(character)
    #         encrypted_block += (num**eee)% nnn 
    #     encrypted_txt += str(encrypted_block)+" "
    # return encrypted_txt

def decrypt(ddd, modulus, encrypted_input):
    decrypted_blocks = []
    for block in encrypted_input:
        block = (block**ddd) % modulus
        decrypted_blocks.append(block)
    return decrypted_blocks



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
    txt_blocks = block_encoder(txt[0], block)
    ddd,phi_n = private_key(ppp, qqq, eee)
    print(txt_blocks)

    print(f"ppp= {ppp}\nqqq= {qqq}\neee= {eee}\nblock= {block}\nmodulus= {modulus}\nddd= {ddd}")
    print(f"eee: {eee} * ddd: {ddd} = 1 mod phi_n:{phi_n}")
    test= eee*ddd
    modtest = 1%phi_n
    print(test)
    print(modtest)
    rsa_list = encrypt(txt_blocks, eee, modulus)
    print(f"rsa_list: {rsa_list}")
    # plain_text_blocks = decrypt(ddd, modulus, rsa_list)
    # print(f"plain_text_block: {plain_text_blocks}")



#Procedures


main()