from psw_gen import Password
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a password.")
    parser.add_argument('--elements', help="password generated from", type=str)
    parser.add_argument('--length', help="length of password", type=int)
    args = parser.parse_args()

    psw = Password(args.elements, args.length)
    psw.generate()
    