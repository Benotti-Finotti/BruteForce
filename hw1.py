#Benjamin Finotti
#January 29th, 2019
#Dr. Drawert
import sys
import hashlib
import os
import string
import itertools
import getpass
import pcrypt
import math
import time

# Works as intended, I believe..
def read_in_username():
    username = input('Your username: ')
    print("Your username is: " + username)
    password = getpass.getpass("Enter password: ")
    entropy = math.log(94, 2) * len(password)
    with open("password.txt", 'a+') as fd:
        fd.write(username + ":")
        fd.write(pcrypt.crypt(password, salt='a5') + "\n")
    print("\nEntropy is: " + str(entropy))


# entropy = math.log(94, 2) * len(password)

# This is only cracking the most recent password.
def brute_force():
    start = time.time()
    with open("password.txt", 'r') as fd:
            sep = ':'
            line = fd.read().splitlines()
            for x in line:
                line = str(line).split(":", 1)[-1]
            for i in itertools.product(string.printable, repeat=3):
                password = ''.join(i)
                print(password)
                i = pcrypt.crypt(password, salt='a5')
                print(line)
                print(i)
                if i + "']" == line:
                    print("Found your password: " + password)
                    print("%s seconds taken" % (time.time() - start))
                    time.sleep(30)
                else:
                    print("Could not find your password.")

if __name__ == "__main__":
    read_in_username()
    brute_force()
    #password = input("Enter hashed value: ")
    #dict_attack(password)