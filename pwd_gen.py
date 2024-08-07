import random
import array

#Password Length
password_len = 16

#Characters to be used
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/']

#Combine all character arrays
all = digits + lower + upper + symbols

#Randomizer
random_digits = random.choice(digits)
random_lower = random.choice(lower)
random_upper = random.choice(upper)
random_symbols = random.choice(symbols)

password = ''
for i in range(password_len):
    password += ''.join(random.choice(all))

print (password)