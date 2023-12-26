import pandas as pd 
from collections import defaultdict

def parser_dict(filename):
    df = pd.read_csv(filename)
    d = defaultdict()
    d = {row.letter:row.code for index, row in df.iterrows()} 
    return d 


def parser(user_input):
    uppered_input = user_input.upper()
    d = parser_dict("nato_phonetic_alphabet.csv")
    return [d[letter] for letter in uppered_input]


if __name__== '__main__':
    user_input = input("Give me a word: ")
    print(parser(user_input))
    