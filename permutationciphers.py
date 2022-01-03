"""
See README for project info and requirerments
"""

from message import Message
DEFAULT_KEY = [3, 1, 2, 0]

"""Returns boolean value; True for decryption, false for encryption
Accepts no arguments
"""
def get_mode():
    user_mode = input("Encrypt or Decrypt this file? (e/d)\n>")
    if user_mode.lower() == 'd':
        print("You have selected to decrypt a file.")
        return True
    print("You have selected to encrypt a file.")
    return False

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
    key = input("Enter (press enter to use default key or see README for info on acceptable keys)\n>")
    if key == '':
        return DEFAULT_KEY
    key_list = []
    for value in key:
        key_list.append(int(value))
    return key_list

"""Returns tuple with two String arguments
First contains filedata to be encrypted/decrypted, second contains key used for encryption/decryption
"""
def parse_file_data(filename):
    #reads file to convert message to appropriate format
    file_contents = open(filename).read()
    file_text = ''.join(file_contents.split()) #removes All whitespace
    file_text = file_text.lower()
    return file_text

def write_new_data(filename, filetext):
    dest_file = open(filename, 'w')

    text_list = []
    for i in range(len(filetext)//5):
        text_list.append(filetext[i*5:i*5+5])

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
    message = Message(key, data, not encrypt)

    message.permutate()

    print(message.text)

    print("Enter desination for message")
    new_filename = get_filename()
    write_new_data(new_filename, message.text)

    if input("Run again (y)?\n>").lower() == 'y':
        main()


if __name__ == '__main__':
    main()
    print("Process ended")
