import random

letters_lower = "a" + "b" + "c" + "d" + "e" + "f" + "g" + "h" + "i" + "j" + "k" + "l" + "m" + "n" + "o" + "p" + "q" + "r" + "s" + "t" + "u" + "v" + "w" + "x" + "y" + "z"
letters_upper = "A" + "B" + "C" + "D" + "E" + "F" + "G" + "H" + "I" + "J" + "K" + "L" + "M" + "N" + "O" + "P" + "Q" + "R" + "S" + "T" + "U" + "V" + "W" + "X" + "Y" + "Z"
numbers = "1" + "2" + "3" + "4" + "5" + "6" + "7" + "8" + "9" + "0"
special_characters = "!" + "@" + "#" + "$" + "%" + "^" + "&" + "*" + "(" + ")"

all_characters = (letters_lower + letters_upper + numbers + special_characters)

#print(len(all_characters))

#print(all_characters[0][0])

my_strong_password = ""

password_length = 8
i = 1

#print(my_strong_password)

import os, random, string

length = 4
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

my_string = ''.join(random.choice(letters_lower) for i in range(length)) + ''.join(
    random.choice(letters_upper) for i in range(length)) + ''.join(
    random.choice(letters_upper) for i in range(length)) + ''.join(
    random.choice(special_characters) for i in range(length))

#print(''.join(random.choice(all_characters) for i in range(length)))
#print(my_string)

my_strong_password = random.sample(my_string, len(my_string))
my_strong_password = ''.join(my_strong_password)

weak_passwords = ["password", "redsox", "babygirl"]

ask = input("Enter strong or weak: ")
if ask == "strong":
    print(my_strong_password)
else:
    print(''.join(random.choice(weak_passwords) for i in range(1)))