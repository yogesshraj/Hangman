import string
import random

def load_words():
    a=open("words.txt")
    b=a.read()
    c=b.split(" ")
    word_list = c
    return word_list

def choose_word():
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word
