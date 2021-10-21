import random
import string

def GeneratePassword():
    # get random password pf length 8 with letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(16))
    return password

def GeneratePassword1():
    # get random password pf length 8 with letters, digits, and symbols
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(16))
    return password

if __name__ == '__main__':
    print(GeneratePassword1())

#Reference: https://pynative.com/python-generate-random-string/