from pystyle import *
from random import *

ft = """

 ▄▄▄▄▄▄                                                                      ▄▄ 
 ██▀▀▀▀█▄                                                                    ██ 
 ██    ██   ▄█████▄  ▄▄█████▄  ▄▄█████▄ ██      ██  ▄████▄    ██▄████   ▄███▄██ 
 ██████▀    ▀ ▄▄▄██  ██▄▄▄▄ ▀  ██▄▄▄▄ ▀ ▀█  ██  █▀ ██▀  ▀██   ██▀      ██▀  ▀██ 
 ██        ▄██▀▀▀██   ▀▀▀▀██▄   ▀▀▀▀██▄  ██▄██▄██  ██    ██   ██       ██    ██ 
 ██        ██▄▄▄███  █▄▄▄▄▄██  █▄▄▄▄▄██  ▀██  ██▀  ▀██▄▄██▀   ██       ▀██▄▄███ 
 ▀▀         ▀▀▀▀ ▀▀   ▀▀▀▀▀▀    ▀▀▀▀▀▀    ▀▀  ▀▀     ▀▀▀▀     ▀▀         ▀▀▀ ▀▀ 
                                                                                
                                                                                
                                by regicidekk                                         
             ▄▄▄▄▄▄▄▄                                                                       
             ██▀▀▀▀▀▀                                                                       
             ██         ▄████▄    ██▄████   ▄███▄██   ▄████▄                                
             ███████   ██▀  ▀██   ██▀      ██▀  ▀██  ██▄▄▄▄██                                   
             ██        ██    ██   ██       ██    ██  ██▀▀▀▀▀▀                               
             ██        ▀██▄▄██▀   ██       ▀██▄▄███  ▀██▄▄▄▄█                               
             ▀▀          ▀▀▀▀     ▀▀        ▄▀▀▀ ██    ▀▀▀▀▀                                
                                            ▀████▀▀            


"""

print(Colorate.Horizontal(Colors.green_to_cyan, ft))

ultalphabet= [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z',
    '1','2','3','4','5','6','7','8','9'
]

upperalph= [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z',
]

loweralph= [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z'
]

alphabet2reg= [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z'
]

nums= [
    '1','2','3','4','5','6','7','8','9'
]

print(Colorate.Horizontal(Colors.green_to_cyan,"what language do you want to use?"))
lang = int(input(Colorate.Horizontal(Colors.green_to_cyan,"1.English\n2.Russian\n ")))
if lang == 1:
    long = int(input(Colorate.Horizontal(Colors.green_to_cyan,"how many characters do you need for a password?\n ")))
    numbers = int(input(Colorate.Horizontal(Colors.green_to_cyan,"1.only numbers\n2.only letter\n3.numbers and letter\n ")))
    if numbers == 1:
        result = ''.join(map(str, choices(nums, k=long)))
        print(Colorate.Horizontal(Colors.green_to_cyan,f"your password: {result}"))
        input("Press Enter to exit...")
    elif numbers == 2:
        rgstr = int(input(Colorate.Horizontal(Colors.green_to_cyan,"what register do you need?\n1.UPPER\n2.lower\n3.bOtH\n ")))
        if rgstr == 1:
            result = ''.join(map(str, choices(upperalph, k=long)))
            print(Colorate.Horizontal(Colors.green_to_cyan,f"your password: {result}"))
            input("Press Enter to exit...")
        elif rgstr == 2:
            result = ''.join(map(str, choices(loweralph, k=long)))
            print(Colorate.Horizontal(Colors.green_to_cyan,f"your password: {result}"))
            input("Press Enter to exit...")
        elif rgstr == 3:
            result = ''.join(map(str, choices(alphabet2reg, k=long)))
            print(Colorate.Horizontal(Colors.green_to_cyan,f"your password: {result}"))
            input("Press Enter to exit...")
    elif numbers == 3:
        result = ''.join(map(str, choices(ultalphabet, k=long)))
        print(Colorate.Horizontal(Colors.green_to_cyan,f"your password: {result}"))
        input("Press Enter to exit...")

if lang == 2:
    long = int(input(Colorate.Horizontal(Colors.green_to_cyan,"сколько символов нужно вашему паролю?\n ")))
    numbers = int(input(Colorate.Horizontal(Colors.green_to_cyan,"1.только числа\n2.только буквы\n3.и буквы и числа\n ")))
    if numbers == 1:
        result = ''.join(map(str, choices(nums, k=long)))
        print(Colorate.Horizontal(Colors.green_to_cyan,f"ваш пароль: {result}"))
        input("нажмите Enter для выхода...")
    elif numbers == 2:
        rgstr = int(input(Colorate.Horizontal(Colors.green_to_cyan,"какой регистр вам нужен?\n1.ВЕРХНИЙ\n2.нижний\n3.оБа\n ")))
        if rgstr == 1:
            result = ''.join(map(str, choices(upperalph, k=long)))
            print(Colorate.Horizontal(Colors.green_to_cyan,f"ваш пароль: {result}"))
            input("нажмите Enter для выхода...")
        elif rgstr == 2:
            result = ''.join(map(str, choices(loweralph, k=long)))
            print(Colorate.Horizontal(Colors.green_to_cyan,f"ваш пароль: {result}"))
            input("нажмите Enter для выхода...")
        elif rgstr == 3:
            result = ''.join(map(str, choices(alphabet2reg, k=long)))
            print(Colorate.Horizontal(Colors.green_to_cyan,f"ваш пароль: {result}"))
            input("нажмите Enter для выхода...")
    elif numbers == 3:
        result = ''.join(map(str, choices(ultalphabet, k=long)))
        print(Colorate.Horizontal(Colors.green_to_cyan,f"ваш пароль: {result}"))
        input("нажмите Enter для выхода...")