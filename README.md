# Random Password Generator
## Overview
The codes generate random passwords using the random combination of lowercase, uppercase letters, number digits and symbols.

Two ways to play with:
1. Default mode: do not assign any elements for passwords to generate from. In this mode, elements as follows:
     - UPPCASE LETTERS: A - Z
     - lowercase letters: a - z
     - numbers: 0 - 9
     - symbols: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    ___Notice:___ Default mode will generate 6-digit password using elements listed above.

2. Customized mode: it allows users to type in any characters and length of password they'd like to.


## How to Run
This program can be executed directly in the terminal as follows:

1. In default mode (as mentioned above), just type in as below:
```
python main.py
```

2. In customized mode, just type in as below:
```
python main.py --elements abcdeABCDE12345 --length 10
```
___Notice:___ either `--elements` and `--length` is a must.
