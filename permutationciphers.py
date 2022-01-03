"""
See README for project info and requirerments
"""

DEFAULT_KEY = '3120'

"""
stores message data; used to access text, encrypt message, decrypt message
"""
class Message():
    def __init__(self, key, text, encrypt):
        self.key = key
        self.text = text
        self.encrypted = not encrypt #is message encrypted? (if we want to encrypt, message is not encrypted)

    #void; encrypts self.text using a permutation cipher with key self.key
    def encrypt(self, text=None):

        blocks = len(self.text) // 4
        encrypted_text = ''

        for i in range(blocks):
            temp = '' #stores the permutated block
            for dig in range(4):
                #self.key[dig] returns the position of the character in plaintext that belongs at index dig in the encrypted text
                # '+ 4*i' adjusts the value according to which block we are in
                temp+= self.text[int(self.key[dig]) + 4*i]
            #after we permutate a block, append the permutated text to encrypted_text
            encrypted_text += temp

        self.text = encrypted_text
        self.encrypted = True

    #void; decrypts self.text using a permutation cipher with key self.key
    def decrypt(self, text=None):
        #uses similar process to encrypt() method

        blocks = len(self.text) // 4
        decr_text = ''

        for i in range(blocks):
            #list used to support assingment
            temp = [''] * 4

            for dig in range(4):
                #use the key to determine where each digit came from and assign it to that position in temp
                temp[int(self.key[dig])] = self.text[dig + 4*i]
            #convert temp to string
            temp = ''.join(temp)
            decr_text += temp

        self.text = decr_text
        self.encrypted = False

"""Returns boolean value; True for encryption, False for decryption
Accepts no arguments
"""
def get_mode():
    user_mode = input("Type 'e' to encrypt a file or 'd' to decrypt a file. Default option is encryption.\n>")
    if user_mode.lower() == 'd':
        print("You have selected to decrypt a file.")
        return False
    print("You have selected to encrypt a file.")
    return True

"""Returns String value with local filename or full filepath
Accepts no arguments
"""
def get_filename():
    filename = input("Enter path of data file.\n>")
    rfilename = repr(filename)[1:-1] #converts to rawstring to prevent escape characters
    return rfilename

"""Returns String value containing encryption key
Accepts no arguments
User supplied key must be a permutation of the digits 0123, otherwise default key will be used
"""
def get_key():
    key = input("Enter four digit numeric key.\n>")
    key_list = list(key)
    key_list.sort()
    if key.isnumeric() and key_list == ['0', '1', '2', '3']:
        print("Key received, proceeding with key " + key)
        return key
    else:
        print("Invalid key, proceeding with default key")
        return DEFAULT_KEY

"""Returns tuple with two String arguments
First contains filedata to be encrypted/decrypted, second contains key used for encryption/decryption
"""
def parse_file_data(filename):
    #reads file to extract data, key, and whether we encrypt or decrypt
    file_contents = open(filename).read()
    file_text = ''.join(file_contents.split()) #removes All whitespace
    file_text = file_text.lower()
    #ensure number of characters in text is a multiple of four
    if len(file_text) % 4 != 0:
        addtn_char = 'e'
        file_text += 'e' * (4 - (len(file_text) % 4))

    return file_text

def write_new_data(filename, filetext):
    dest_file = open(filename, 'w')

    text_list = []
    for i in range(len(filetext)//4):
        text_list.append(filetext[i*4:i*4+4])

    formatted_text = ' '.join(text_list)
    dest_file.write(formatted_text)
    dest_file.close()

def main():
    print("Start")

    #collect necessary info
    encrypt = get_mode()
    filename = get_filename()
    key = get_key()

    #clean filedata and create message object
    data = parse_file_data(filename)
    message = Message(key, data, encrypt)

    if encrypt:
        message.encrypt()
    else:
        message.decrypt()

    print(message.text)

    print("Enter desination for message")
    new_filename = get_filename()
    write_new_data(new_filename, message.text)

    if input("Run again (y)?\n>").lower() == 'y':
        main()


if __name__ == '__main__':
    main()
    print("Process ended")
