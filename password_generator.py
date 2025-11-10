import os, random,string

def generate_password():


    length= len(input("enter the length of yuo pasword "))
    include_lowercase=input("incluede lowecasse letter?  (yes /no) : ") .strip().lower()
    include_uppercase=input("incluede uppercase letter?  (yes /no) : ") .strip().lower()
    include_spacial=input("incluede spacial letter?  (yes /no) : ") .strip().lower()
    include_digits=input("incluede digits?  (yes /no) : ") .strip().lower()

    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    special=string.punctuation
    digits= string.digits

    total_character = lowercase+ uppercase+ special + digits


    requared_character=[]

    if include_uppercase=="yes":
        requared_character.append(random.choice(uppercase))
    if  include_spacial == "yes":
        requared_character.append(random.choice(special))
    if include_digits== "yes" :
        requared_character.append(random.choice(digits))
        
    remaining_character = length - len(requared_character)
    password = remaining_character

    for _ in range(remaining_character):
        char= random.choice(total_character)
        password.append(char)

        str_password="".join(password)
        random.shuffle(password)
        return str_password
password=generate_password()

generate_password()
print(password)