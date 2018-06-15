# -*- coding: utf-8 -*-
"""Main module."""

# Standard library imports
import random
import string


def check_palindrome(word):
    """Check if a word is a palindrome."""
    word = word.lower()
    reverse = word[::-1]
    return reverse == word


def random_letter(word=None):
    """Return a random letter of the alphabet."""
    if word:
        letters = word
    else:
        letters = string.ascii_letters

    index = random.randint(0, len(letters)-1)
    return letters[index]


def random_int(lower, upper):
    """Return a random integer from the alphabet."""
    return random.randint(lower, upper)
