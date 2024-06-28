import collections

def is_anagram(s: str, t: str) -> bool:
    return collections.Counter(s) == collections.Counter(t)