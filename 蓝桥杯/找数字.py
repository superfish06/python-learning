n = int(input())
nums = list(map(int,input().split()))

def function (nums):
  cnt = 0
  for num in nums:
    fs = int((8*num+1)**0.5)
    if fs**2 != 8*num+1:
      cnt += 1
  return cnt


print(function(nums))