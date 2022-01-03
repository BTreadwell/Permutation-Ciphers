"""
Module used in permutationciphers.py
Contains Message class
"""

#Stores message data and methods used in permutating data
class Message():

    def __init__(self, key=[3,2,1,0], text='abcdefghijklmnopqrstuvwxyz', encrypted=False):

        self.encr_key = key #encryption key
        self.decr_key = self.get_inverse() #decryption key which is inverse of encr key
        self.text = text
        self.validate_text()
        self.encrypted = encrypted

    #returns list; used to find value for self.decr_key during construction
    def get_inverse(self):
        inv_key = [0] * len(self.encr_key)

        for i in range(len(self.encr_key)):
            inv_key[self.encr_key[i]] = i

        return inv_key

    #void; modifies self.text to ensure it is evenly divisible by len(self.encr_key)
    def validate_text(self):
        if len(self.text) % len(self.encr_key) == 0:
            return True
        else:
            self.text += 'z' * (len(self.encr_key) - len(self.text) % len(self.encr_key))
            return True

    #void; permutates self.text using a permutation cipher and appropriate key
    def permutate(self):
        #determine which key to use based on whether the file is encrypted or decrypted
        key = self.encr_key
        if self.encrypted:
            key = self.decr_key

        num_blocks = len(self.text) // len(key)
        permu_text = ''

        for block in range(num_blocks):

            plaintext = self.text[block * len(key):(block+1)*len(key)]
            ciphertext = [0] * len(key) #stores the permutated block

            for i in range(len(key)):
                ciphertext[i] = plaintext[key[i]]
            ciphertext = ''.join(ciphertext)

            #after we permutate a block, append the permutated text to encrypted_text
            permu_text += ciphertext

        self.text = permu_text
        self.encrypted = not self.encrypted

"""
a = Message(key=[5,4,2,0,3,1])
print(a.text)
print(a.encr_key)
a.permutate()
print(a.text)
print(a.decr_key)
a.permutate()
print(a.text)
"""
