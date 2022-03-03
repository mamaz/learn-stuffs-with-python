from collections import Counter

def is_anagram(string: str, comparer: str) ->str:
    if len(string) != len(comparer):
        return False
    return Counter(string) == Counter(comparer)

if __name__ == "__main__":
    print(f"""{is_anagram('kasur rusak', 'kasur rusak')}""")
    print(f"""{is_anagram('aku', 'kui')}""")
