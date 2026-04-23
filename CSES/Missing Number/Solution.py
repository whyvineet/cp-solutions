n = int(input())
nums = list(map(int, input().split()))

total_sum = (n * (n + 1)) // 2
available = sum(nums)

print(total_sum - available)