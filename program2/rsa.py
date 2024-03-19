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


#///////////////////////////////////////////////////
#Input Processsing
#///////////////////////////////////////////////////
def block_encoder(line_input, block_size):
    block_list = []
    counter = block_size-1
    block_item = 0
    line_vals = line_input.split()
    print(line_vals)
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

def unblock(plaintxt_block):
    plain_txt = []
    counter = 0
    while block > 0:
        



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
    ddd = axbm(eee, 1, phi_n)
    return ddd

#///////////////////////////////////////////////////
#Operations
#///////////////////////////////////////////////////

def starstar(aaa, bbb, nnn):
    """ Modular integer exponentiation.
        This computes a^b mod n using the efficient bit representation
        of the exponent.
        Parameters:
            aaa: the base
            bbb: the exponent
            nnn: the modulus
        Returns:
            aaa ^ bbb mod nnn list of the centroids

    """
    runningproduct = 1
    multiplier = aaa
    localexponent = bbb
    while localexponent > 0:
        rightmostbit = localexponent % 2
        if rightmostbit == 1:
            runningproduct *= multiplier
            runningproduct = runningproduct % nnn
        multiplier *= multiplier
        multiplier = multiplier % nnn
        localexponent = localexponent // 2
#        print(f'{localexponent:d} {multiplier:d} {runningproduct:d}'

    return runningproduct

def mymod(aaa, nnn):
    """ Do modular reduction 'aaa mod nnn' returning a positive value.
        Parameters:
            aaa:
            nnn:
        Returns:
            aaa mod nnn as a positive value
    """
    return ((aaa % nnn) + nnn) % nnn

def axbm(ainput, binput, minput):
    """ Compute 'x', such that a*x = b (mod m).
        Returns 'x' as value of function.
        Parameters:
            ainput: the 'a' value
            binput: the 'b' value
            minput: the modulus 'm' value
        Returns:
            'x' that solves the congruence
    """
#    sss = f'\nZORK a, b, m {ainput:4d} {binput:4d} {minput:4d}'
#    print(sss)
    ## If ainput is zero mod minput
    ##     and binput is zero mod minput
    ##         then return 1, since we have 0 = 0
    aaa = mymod(ainput, minput)
    if aaa == 0:
        bbb = mymod(binput, minput)
        if bbb == 0:
#            return -minput
            return 1
        else:
#            print('NOSOLUTION: zero is not zero')
            return -1

    mmm = minput
#    aaa = ((ainput % mmm) + mmm) % mmm ## we assume m is positive?
    aaa = mymod(ainput, mmm)
    qqq = int(mmm//aaa)
    rrr = mmm % aaa
    nnn1 = 0
    nnn2 = 1
    sgn = 1
    while rrr != 0:
        sgn = - sgn
        nnn3 = nnn2 * qqq + nnn1
        nnn1 = nnn2
        nnn2 = nnn3
        mmm = aaa
        aaa = rrr
        qqq = int(mmm//aaa)
        rrr = mmm % aaa

    bbb = int(binput // aaa)
    ttt = binput % aaa
    if ttt != 0:
        print('NOSOLUTION: gcd does not divide b')
        return -aaa

    # The check value 'ttt' is zero, so we have a gcd.
    xxx = (bbb * nnn2) % minput
    if sgn == -1:
        xxx = -xxx
    if xxx < 0:
        xxx += minput
    return xxx

#///////////////////////////////////////////////////
#Output Processing
#///////////////////////////////////////////////////

def ascii_convert(text_input):
    pass

def print_info():
    pass

#///////////////////////////////////////////////////
#Encryption/Decryption    
#///////////////////////////////////////////////////

def encrypt(block_list, eee, modulus):
    encrypted_blocks = []
    for block in block_list:
        encrypted_blocks.append(starstar(block, eee, modulus))
    return encrypted_blocks

def decrypt(ddd, modulus, encrypted_input):
    decrypted_blocks = []
    for block in encrypted_input:
        block = starstar(block, ddd, modulus)
        decrypted_blocks.append(block)
    return decrypted_blocks


#///////////////////////////////////////////////////
#Main Processes
#///////////////////////////////////////////////////

def main():

    #Input Files

    with open("input1pq.txt","r") as fpq:
        pqinputs = fpq.readlines()
    with open("input1text.txt", "r") as ftxt:
        txt = ftxt.readlines()
    pqinputs = striplines(pqinputs)
    txt = striplines(txt)

    #Begin Key-Making
    print(txt[0])
    ppp, qqq, eee, block, modulus = public_key(pqinputs[0])
    txt_blocks = block_encoder(txt[0], block)
    ddd = private_key(ppp, qqq, eee)
    print(f"Text in blocks: {txt_blocks}")

    print(f"ppp= {ppp}\nqqq= {qqq}\neee= {eee}\nblock= {block}\nmodulus= {modulus}\nddd= {ddd}")

    rsa_list = encrypt(txt_blocks, eee, modulus)
    print(f"rsa_list: {rsa_list}")
    plain_text_blocks = decrypt(ddd, modulus, rsa_list)
    print(f"plain_text_block: {plain_text_blocks}")

main()
