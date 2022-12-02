import time
import string
#Below is the encryption function and encrypts the plaintext the user submits.
def encryption():
    Cipher_Type = input("What Cipher type are you using? Options are either 'Ceaser' or 'Basic': ")
#Below is the basic Encryption for the program and has a set shift number of 20 by default. This just makes the program easier.
    encrypted_text = ""
    if Cipher_Type == "Basic":
        User_Text = input("What is your text to be encrypted?: ")
        for letter in User_Text:
            code_letter = ord(letter)

            new_letter_code = code_letter - 20

            changed_letter = chr(new_letter_code)

            encrypted_text += changed_letter
        print(f"Your encrypted message is: {encrypted_text}")
        print("You have 20 seconds till you are sent back to main menu")
        time.sleep(20)
#This is the ceaser encryption where they put in a shift number and the text etc.
    elif Cipher_Type == "Ceaser":
        alphabets = string.ascii_lowercase + string.ascii_lowercase
        text = list(input('Enter your text to be encrypted: \n').lower())
        shiftnum = int(input('What is the shift number? (This should be from 1-25): '))
        for i in range(len(text)):
            if text[i] == ' ':
                text[i] = ' '
            else:
                new_letter = alphabets.index(text[i]) + shiftnum
                text[i] = alphabets[new_letter] 
            output = (''.join(map(str,text)))
        print(f"Your encrypted message is: {output} and your shift was {shiftnum}")
        print("You have 20 seconds till you are sent back to main menu")
        time.sleep(20)
#Any else command in the code runs when a prompt is answered wrong.
    else:
        print("That is not a type please try again.")
        time.sleep(2)
        encryption()
#Decryption function below.
def decryption():
    Cipher_Type = input("What Cipher type are you using? Options are either 'Ceaser' or 'Basic': ")
    
#Below is the basic decryption and the difference between this and ceaser is we do not pick the shift number.
    encrypted_text = ""
    if Cipher_Type == "Basic":
        User_Text = input("What is your encrypted text: ")
        for letter in User_Text:
            code_letter = ord(letter)

            new_letter_code = code_letter + 20

            changed_letter = chr(new_letter_code)

            encrypted_text += changed_letter

        print(f"Your decrypted message is: {encrypted_text}")
        print("You have 20 seconds till you are sent back to main menu")
        time.sleep(20)
#Below is the Ceaser cipher code for decryption. It takes the users encrypted message they have and you choose your shift number and you can decrypt it.
    elif Cipher_Type == "Ceaser":
        alphabets = string.ascii_lowercase + string.ascii_lowercase
        text = list(input('Enter your text to be decrypted: ').lower())
        shiftnum = int(input('What is the shift number? (This should be from 1-25): '))
        for i in range(len(text)):
            if text[i] == ' ':
                text[i] = ' '
            else:
                new_letter = alphabets.index(text[i]) - shiftnum
                text[i] = alphabets[new_letter]
                output = (''.join(map(str,text)))
        print(f"Your decrypted message is: {output} and your shift was {shiftnum}")
        print("You have 20 seconds till you are sent back to main menu")
        time.sleep(20)
#The above section is the Decryption Function. This part of the program decrypts your encrypted message after deciding which encryption you wanted to use etc. 
    else:
        print("That is not a type please try again.")
        time.sleep(2)
        decryption()
#Down below is the menu function.
def Menu():
    on = True
    while on:
        print("""
    ███████ ███████  ██████ ██████  ███████ ████████     ███    ███ ███████ ███████ ███████  █████   ██████  ███████ 
    ██      ██      ██      ██   ██ ██         ██        ████  ████ ██      ██      ██      ██   ██ ██       ██      
    ███████ █████   ██      ██████  █████      ██        ██ ████ ██ █████   ███████ ███████ ███████ ██   ███ █████   
         ██ ██      ██      ██   ██ ██         ██        ██  ██  ██ ██           ██      ██ ██   ██ ██    ██ ██      
    ███████ ███████  ██████ ██   ██ ███████    ██        ██      ██ ███████ ███████ ███████ ██   ██  ██████  ███████ 
                                                                                                             
                                                                                                                    """)
        print("By: Riley Scott")
        print("This program can create secret messages for you and a friend. ENTER THE EXACT TEXT FOR PROMPTS!")
        print("Press 'D' for Decryption of a message.")
        print("Press 'E' for Encryption of a message.")
        print("Type 'Exit' to end the program")
        UserDecsion = input("Enter Here: ")
        if UserDecsion == "D":
            decryption()
        elif UserDecsion == "E":
            encryption()
        elif UserDecsion =="Exit":
            break
        else:
            print("incorrect entry")
            time.sleep(4)
            Menu()
Menu()
#This above is the decision menu and allows a user to select all the things they want. It also allows you to see what this program is called etc.
