def twosum(nums, target):
    num_to_index = {}
    for i,num in enumerate(nums):
        if target - num in num_to_index:
            return [num_to_index[target-num],i]
        num_to_index[num] = i
    return []
print (twosum([2,7,11,15],9))
