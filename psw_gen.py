#%%
import string
import random

class Password():
    
    def __init__(self, elements=None):
        
        # memebers in password
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        nums = "".join(list(map(str, range(10))))
        symbles = "[]{}()*;/,_-@"

        # join all memembers above together
        self.cmb = lower + upper + nums + symbles

        # length of the password
        self.length = 16

    def generate(self):
        # generate random password
        psw = "".join(random.sample(self.cmb, self.length))
        return psw

psw1 = Password()
print(psw1.generate())
