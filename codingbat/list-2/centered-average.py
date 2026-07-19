def centered_average(nums):
  total = sum(nums) - min(nums) - max(nums)
  count = len(nums) - 2
  return total // count
