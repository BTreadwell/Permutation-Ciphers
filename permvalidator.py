#Used to validate input/values

class KeyError(Exception):
    """Raised when there is an issue with the supplied key"""
    pass

class FileError(Exception):
    """Raised when there is an issue finding or creating the file"""
    pass

def validate_key(key):
    #ensure key is a list
    if type(key) != list:
        print(type(key))
        raise KeyError
    #list values should be integers
    for value in key:
        if type(value) != int:
            print(value)
            raise KeyError
    #list should contain values starting at zero up to one less than the length of the list
    else:
        key.sort()
        if key != list(range(len(key))):
            print('else')
            raise KeyError

def validate_source(source):
    try:
        open(source)
    except:
        raise FileNotFoundError

def validate_dest(dest):
    try:
        open(dest)
    except:
        raise FileError
def validate(a_key='0123', a_source='data.txt', a_dest='new_data.txt', strict=True):
    try:
        validate_key(a_key)
        validate_source(a_source)
        validate_dest(a_dest)
    except:
        return False
    else:
        return True
#Testing for validate_key
"""
a = 1234
try:
    validate_key(a)
except KeyError:
    print(a)
a = ['1', '0', '2', '3']
try:
    validate_key(a)
except KeyError:
    print(a)
a = [1, 0, 3, 4, 2]
try:
    validate_key(a)
except KeyError:
    print(a)
a = [1, 2, 3, 4]
try:
    validate_key(a)
except KeyError:
    print(a)
"""
