from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    hmap = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        hmap[tuple(count)].append(word)

    return list(hmap.values())