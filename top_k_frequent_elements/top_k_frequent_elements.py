import collections

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = collections.Counter(nums)

    freq = [[] for _ in range(len(nums)+1)]
    for v,c in count.items():
        freq[c].append(v)

    res = []
    for i in range(len(freq)-1, 0, -1):
        if len(freq) == 0:
            continue
        res.extend(freq[i])
        if len(res) >= k:
            break
    return res[:k]