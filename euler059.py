#!/usr/bin/env python3

# XOR decryption
# Problem 59
#
# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange).
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key.
# The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes.
# The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
# If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
# The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower case characters.
# Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

from functools import reduce

with open('p059_cipher.txt') as f:
    data = f.read()

encrypted = list(map(int, data.split(',')))
length = len(encrypted)
lowercase = range(97, 123)

the_best = 0  # the highest number of 'the' in the decrypted message
result = 0

for k0 in lowercase:
    for k1 in lowercase:
        for k2 in lowercase:
            # create a list of the same length as _encrypted_ with the key repeated cyclically
            xor = length//3 * [k0, k1, k2] + [k0, k1, k2][:length % 3]
            # decrypt the file and convert it to string
            decrypted = ''.join([chr(a ^ b) for a, b in zip(encrypted, xor)])
            # find number of occurrences of the most common English word
            the = decrypted.count(' the ')

            if the > the_best:
                # the current message is most likely to be a plain text in English
                the_best = the
                # convert back from string to ASCII values first and then add them all
                result = reduce(lambda x, y: x + y, map(ord, decrypted))

print ("Result:", result)
