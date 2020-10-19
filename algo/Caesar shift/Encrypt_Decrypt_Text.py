def encrypt(text,key): 
    output = "" 
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            output += chr((ord(char) + key - 65) % 26 + 65)
        elif (char.islower()): 
            output += chr((ord(char) + key - 97) % 26 + 97) 
        else:
            output += char
    return output 

def decrypt(text,key): 
    output = "" 
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            output += chr((ord(char) - 65 - key) % 26 + 65)
        elif (char.islower()): 
            output += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            output += char 
    return output 

message = input('Enter your message:')
choice = input('What do you want to do?\nType 1 for encrypt:\nType 2 for decrypt:\n')

if (int(choice) == 1):
    shift = input('Enter your key to encrypt (numbers to be shift):')
    message = encrypt(message, int(shift))
    print('Your encrypt message is: ', message)
    exit()
    
elif (int(choice) == 2):
    key = input('Enter your key for decryping (number that has been shifted):')
    message = decrypt(message, int(key))
    print('Your decrypt message is:', message)
    exit()

else:
    print('Error, Terminated.')
    exit()
