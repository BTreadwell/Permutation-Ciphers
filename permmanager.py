"""
*****************************************************
See README for project info and requirerments
*****************************************************
Dependencies: message.py, permvalidator.py

Program can be used as stand alone CL application or users can use permciphersGUI.py
which implements permmanager with PyQt5 to create a GUI application.
"""

import message, permvalidator
DEFAULT_KEY = [5, 3, 1, 4, 0, 2]
#Good
"""Return type; int
Gets user input to determine if key or inv key should be used; 0 for key; 1 for inverse key
accepts no arguments
"""
def get_mode():
    mode = input('Encrypting a file will apply a permutation cipher using the provided key. Decrypting will apply a permutation cipher using the inverse of the provided key. Do you want to encrypt or decrypt (e/d)?\n>')
    if mode.lower() == 'd':
        return 1
    elif mode.lower() == 'e':
        return 0
    else:
        print("We can't recognize that input; proceeding with file encryption.")
        return 0
#good
"""Return type; String
Gets user input for local filename or full filepath
Accepts 1 String argument that specifies whether the file is for the source or destination
"""
def get_filename(dest_source):
    filename = input("Enter path of {} file.\n>".format(dest_source))
    rfilename = repr(filename)[1:-1] #converts to rawstring to prevent escape characters; slice to remove ' at beginning and end
    return rfilename
#good
"""Return type; List[Ints]
Gets user input for encryption key and
Accepts no arguments
"""
def get_key():
    key = input("Select encryption key (press enter to use default key or see README for info on acceptable keys)\n>")
    if key == '':
        return DEFAULT_KEY
    key_list = []
    try:
        for value in key:
            key_list.append(int(value))
    except ValueError:
        print("Can't process that key. Try again.")
        get_key()
    return key_list
#good
"""Return type; String
Removes whitespace and converts text to lowercase
Accepts 1 String argument containing filename/location of message
"""
def parse_file_data(filename):
    #reads file to convert message to appropriate format
    file_contents = open(filename).read()
    file_text = ''.join(file_contents.split()) #removes all whitespace
    file_text = file_text.lower()
    return file_text
#good; can work on formatting outputted text
"""Void type;
Writes text to specfied file
Accepts 2 String arguments containg name of file to write to, and what to write
"""
def write_new_data(filename, filetext):
    dest_file = open(filename, 'w')
    """
    text_list = []
    for i in range(len(filetext)//5):
        text_list.append(filetext[i*5:i*5+5])

    formatted_text = ' '.join(text_list)
    dest_file.write(formatted_text)
    """
    dest_file.write(filetext)
    dest_file.close()

"""Void type;
creates message object, permutates text, and writes permutated text to file
Accepts 4 arguments, type bool, type list[int], and 2 type strings
"""
def process_request(a_mode=0, a_key=DEFAULT_KEY, a_source='data.txt', a_dest='new_data.txt'):
        #clean filedata and create message object
        data = parse_file_data(a_source)
        new_message = message.Message(a_key, data, a_mode)
        #permutate message
        new_message.permutate()
        #write output
        write_new_data(a_dest, new_message.text)


"""Void type;
called in main to run CL program
no argument 
"""
def engine():

    run = True
    while run:
        mode = get_mode()
        source_file = get_filename('source')
        key = get_key()
        dest_file = get_filename('destination')
        is_valid = permvalidator.validate(a_key=key, a_source=source_file, a_dest = dest_file)
        if is_valid:
            process_request(a_mode=mode, a_key=key, a_source=source_file, a_dest=dest_file)
            run_again = input("Would you like to run the program again? (y/n)")
            if run_again.lower() == 'n':
                run = False
        else:
            print("We're having trouble handling that request, let's try again")

def main():
    print("Program Started")
    engine()
    print("Program Ended")

if __name__ == '__main__':
    main()
