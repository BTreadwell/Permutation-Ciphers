"""
See README for project info and requirerments
"""

"""
Return: String
Args: None
"""

class Message():
    def __init__(self, key, text):
        self.key = key
        self.text = text

    def encrypt(self, text=self.text):
        etxt = ''
        return etxt

    def decrypt(self, text=self.text):
        dtxt = ''
        return dtxt

def get_filename():
    filename = input("Enter path of data file: ")
    rfilename = repr(filename)[1:-1] #converts to rawstring to prevent escape characters
    return rfilename

def parse_file_data(filename):
    #reads file to extract data, key, and whether we encrypt or decrypt
    file_data = ''
    key = ''
    encrypt = ''
    return file_data, key, encrypt

def write_new_data(filename, key, encrypt):
    pass

def main():
    print("Start")
    filename = get_filename()
    data, key, encrypt = parse_file_data(filename)
    message = Message(key, data)
    new_data = ''
    if encrypt:
        new_data = message.encrypt()
    else:
        new_data = message.decrypt()
    new_filename = ''
    write_new_data(new_filename, key, not encrypt)
    if input("Continue (y)?") == 'y':
        main()
    print("End")


if __name__ == '__main__':
    main()
    print('end')
