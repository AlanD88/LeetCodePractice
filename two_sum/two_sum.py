def two_sum(nums: list[int], target: int) -> list[int]:
    hmap = {}
    for idx, num in enumerate(nums):
        if hmap.get(target-num) is not None:
            return [hmap.get(target-num), idx]
        hmap[num] = idx