"""
See README for project info and requirerments
"""

DEFAULT_KEY = '3120'

class Message():
    def __init__(self, key, text):
        self.key = key
        self.text = text

    def encrypt(self, text=None):
        etxt = ''
        return etxt

    def decrypt(self, text=None):
        dtxt = ''
        return dtxt

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
    return file_text

def write_new_data(filename, filetext):
    pass

def main():
    print("Start")

    #Following block: Get necessary info from user input using functions
    encrypt = get_mode()
    filename = get_filename()
    key = get_key()


    data = parse_file_data(filename)
    message = Message(key, data)

    if encrypt:
        message.encrypt()
    else:
        message.decrypt()

    new_filename = get_filename()

    write_new_data(new_filename, message.text)
    if input("Run again (y)?\n>").lower() == 'y':
        main()


if __name__ == '__main__':
    main()
    print("Process ended")
