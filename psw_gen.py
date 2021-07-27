#%%
import string
import random


# memebers in password
lower = string.ascii_lowercase
upper = string.ascii_uppercase
nums = "".join(list(map(str, range(10))))
symbles = "[]{}()*;/,_-@"

# join all memembers above together
cmb = lower + upper + nums + symbles

# length of the password
length = 16

# generate random password
psw = "".join(random.sample(cmb, length))

print(psw)

