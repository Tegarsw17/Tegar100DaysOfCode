def twoSum(nums, target):
    i = 1
    ans = []
    while len(nums) > i:
        v = nums[i:]
        for j in range(len(v)):
            if(nums[i - 1] + v[j]) == target:
                s = [i - 1, j + i]
                ans.extend(s)
                break
        i = i + 1
    print(ans)


twoSum([1, 2, 3, 5], 6)
twoSum([3, 3], 6)
