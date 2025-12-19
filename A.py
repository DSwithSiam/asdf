
def subsets(nums):
    n = len(nums)
    result = []

    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)

    return result

print(subsets([1, 2, 3]))
