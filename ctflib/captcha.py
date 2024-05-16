#!/usr/bin/env python3
import hashlib
import secrets
import time

# Load flag
flag = 'flag{this-is-an-example-flag}'
with open('flag.txt') as f:
	flag = f.read().strip()

# A great cli challenge needs a great visual
print('''
      ██████╗ █████╗ ██████╗ ████████╗ ██████╗██╗  ██╗ █████╗       
     ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔══██╗      
     ██║     ███████║██████╔╝   ██║   ██║     ███████║███████║      
     ██║     ██╔══██║██╔═══╝    ██║   ██║     ██╔══██║██╔══██║      
     ╚██████╗██║  ██║██║        ██║   ╚██████╗██║  ██║██║  ██║      
      ╚═════╝╚═╝  ╚═╝╚═╝        ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝      
 ██╗  ██╗    ██╗  ██╗██╗   ██╗███╗   ███╗ █████╗ ███╗   ██╗███████╗ 
 ██║  ██║    ██║  ██║██║   ██║████╗ ████║██╔══██╗████╗  ██║██╔════╝ 
 ███████║    ███████║██║   ██║██╔████╔██║███████║██╔██╗ ██║███████╗ 
 ╚════██║    ██╔══██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║╚════██║ 
      ██║    ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║███████║ 
      ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ 
''')

# Create a random hash
random_hash = secrets.token_hex(3)[:5]
# Ask user to break the hash
print("Please prove that you are not a human!")
answer = input('Enter a string whose MD5 hash starts with "' + random_hash + '"\n> ')

print("")
print("Processing input ... ")
time.sleep(1.2)
print("Pip pup piip ... ")
time.sleep(1.5)
print("")

# Check user input
given_hash = hashlib.md5(answer.encode()).hexdigest()[:5]
if random_hash == given_hash:
	print("Congrats!! Here is your flag --> " + flag)
else:
	print("That doesn't seem correct :/ ")
