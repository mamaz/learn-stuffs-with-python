from typing import Dict
from collections import Counter

def count_word(words: str) -> Dict:
    word_list = words.split(' ')
    word_dict = {}
    for word in word_list:
        if word_dict.get(word):
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict

def count_word_counter(words: str) -> Dict:
    return Counter(words.split(' '))

if __name__ == "__main__":
    print(count_word_counter('akui aku aku lagi'))


