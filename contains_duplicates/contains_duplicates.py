def contains_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))