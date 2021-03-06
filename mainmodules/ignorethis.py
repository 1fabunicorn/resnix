from __future__ import print_function
import re
"""
    vigenere cipher
    Copyright (C) 2017,  Nova Trauben, noah.trauben@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


def encrypt(plaintext, key):
    """

    :param plaintext: unencrypted text
    :param key: encryption key
    :return: returns cyphertext
    """
    cyphertext = []
    len_of_key = len(key)

    for keyindex, plaintext in enumerate(plaintext):
        cyphertext.append(ord(plaintext) + ord(key[keyindex % len_of_key]) % 255)
    return re.sub('[\[\],]', '', str(cyphertext))


def decrypt(cyphertext, key):
    """

    :param cyphertext: encrypted plaintext
    :param key: encryption key
    :return: return plaintext
    """
    plaintext = []
    len_of_key = len(key)

    for keyindex, numbers in enumerate(cyphertext):
        if numbers > 255 or numbers < 0:
            raise ValueError

        plaintext.append(chr(numbers - ord(key[keyindex % len_of_key]) % 255))
    return "".join(plaintext)
