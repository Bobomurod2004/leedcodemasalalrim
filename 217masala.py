def containsDuplicate(nums):
    for x in nums:
        return  len(nums) != len(set(nums))
nums = [3,1]
natija=containsDuplicate(nums=nums)
print(natija)

# nums = [1, 2, 3, 4]
# for x in nums:
#     for y in x:
#
