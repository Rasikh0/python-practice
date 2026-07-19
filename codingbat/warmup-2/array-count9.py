def array_count9(nums):
  count = 0
  nine = 9
  for i in nums:
    if i == nine:
      count += 1
  return count
