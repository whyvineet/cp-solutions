n = int(input())
nums = list(map(int, input().split()))

result = 0
curr_max = nums[0]
for i in range(1, n):
    curr_max = max(curr_max, nums[i])
    result += (curr_max - nums[i])

print(result)