#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
rndm = 0
chars = 0
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
chars += nr_letters
nr_symbols = int(input(f"How many symbols would you like?\n"))
chars += nr_symbols
nr_numbers = int(input(f"How many numbers would you like?\n"))
chars += nr_numbers

#Hard Verions: Generates in a random order. Loop continues until conditions have been met.

pword = []
while (nr_letters > 0 or nr_symbols > 0 or nr_numbers > 0):
  for rndm in range(0,chars):
    rando = random.randint(0,2)
    if(rando == 0): #and (nr_letters > 0)):
      if nr_letters > 0:
        ltr = random.choice(letters)
        pword.append(ltr)
        nr_letters = int(nr_letters) - 1
        chars -= 1
    if(rando == 1) :#and (nr_letters > 0)):
       if nr_symbols > 0:
        sym = random.choice(symbols)
        pword.append(sym)
        nr_symbols = int(nr_symbols) - 1
        chars -= 1
    if(rando == 2) :#and (nr_letters > 0)):
      if nr_numbers > 0:
        nbr = random.choice(numbers)
        pword.append(nbr)
        nr_numbers = int(nr_numbers) - 1
        chars -= 1
    
if chars == 0:
  print("Your password is: ")
  print(''.join(pword))