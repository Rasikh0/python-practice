def count_evens(nums):
  even_total = 0
  for num in nums:
    if num%2 == 0:
      even_total += 1
  return even_total
