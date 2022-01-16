"""
Contains Message class which is used to store information on text in addtion
to methods used to encrypt it using a permutation cipher.
Used in permmanager.py
"""

"""
Stores message data and methods used in permutating data
default constructor takes three arguments; List[int], String, boolean
"""
class Message():

    def __init__(self, key, text, encrypted=0):

        self.encr_key = key #String; used to encrypt
        self.decr_key = self.get_inverse() #String; inverse of encr_key; used to decrypt

        self.text = text #String
        self.normalize_text() #ensures text length is evenly divisible by key length

        self.encrypted = encrypted #Boolean

    """
    Return type, List[Int]
    Computes inverse key of self.encr_key
    Accepts no arguments
    """
    def get_inverse(self):
        inv_key = [0] * len(self.encr_key)

        for i in range(len(self.encr_key)):
            inv_key[self.encr_key[i]] = i

        return inv_key

    """
    Void
    Adds 'z' characters to the end of the message to ensure it is divisible by key length
    Accepts no arguments
    """
    def normalize_text(self):
        if len(self.text) % len(self.encr_key) != 0:
            self.text += 'z' * (len(self.encr_key) - len(self.text) % len(self.encr_key))

    """
    Void
    Permutates text using a permutation cipher and either encr_key or decr_key based on self.encryption
    Accepts no arguments
    """
    def permutate(self):
        #determine which key to use based on whether the file is encrypted or decrypted
        key = self.encr_key
        if self.encrypted:
            key = self.decr_key

        num_blocks = len(self.text) // len(key)
        permu_text = ''

        for block in range(num_blocks):

            plaintext = self.text[block * len(key):(block+1)*len(key)]
            ciphertext = [' '] * len(key) #stores the permutated block

            for i in range(len(key)):
                ciphertext[i] = plaintext[key[i]]
            ciphertext = ''.join(ciphertext)

            #after we permutate a block, append the permutated text to encrypted_text
            permu_text += ciphertext

        self.text = permu_text
        self.encrypted = not self.encrypted
