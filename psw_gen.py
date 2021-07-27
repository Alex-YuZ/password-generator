import string
import numpy as np

class Password():
    
    def __init__(self, elements=None, length=None):
        """[summary]

        Args:
            elements (str, optional): elements used to generate password. Defaults to None.

            length (int, optional): length of password. Defaults to None.
            
        Example_1:
            psw1 = Password()
            psw1.generate()
            
        Example_2:
            psw2 = Password("ABCXYZabc0123@#$", 6)
            psw1.generate()
        """
        
        if elements is None:
            # memebers in password
            lower = string.ascii_lowercase
            upper = string.ascii_uppercase
            nums = "".join(list(map(str, range(10))))
            symbols = "".join(list("""!"\#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""))

            # join all memembers above together
            self.cmb = lower + upper + nums + symbols
            
        else:
            self.cmb = elements

        if length is None:
            # length of the password
            self.length = 6
   
        else:
            self.length = length

    def generate(self):
        """generate the password"""
        
        self.psw = "".join(np.random.choice(list(self.cmb), self.length))
        print(self.psw)
        # return self.psw
    
    def __str__(self):
        return "This is an instance of Password class"
    
    def __repr__(self):
        return "CLASS OBJECT: Password(elements, length)".format()

