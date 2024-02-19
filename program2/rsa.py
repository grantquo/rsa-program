"""
/////////////////////////////////////////////////////////////////////
rsa.py
Main encryption/decryption file for RSA. Takes inputs for encryption
or decryption, processing them through RSA and outputting the result.
/////////////////////////////////////////////////////////////////////
"""
import sys
import os


os.chdir("/home/kingkoobie/cs401/program2")

#Take Input
with open("input1.txt","r") as f:
    startingtext = f.read()


#Present Input String
def get_input(text):
    text_char = ""
    data_list = text.split()
    for iii in data_list:
        print(iii)
        int_iii = int(iii)
        text_char += chr(int_iii)
    return print(text_char)


def block_splitter():
    pass

def main():
    pass

print(startingtext)
get_input(startingtext)
main()