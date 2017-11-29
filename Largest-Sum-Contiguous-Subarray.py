def maxSubArray(alist):
  maxSum = 0
  maxArraySum = 0
  
  for i in range(len(alist)):
    maxArraySum = maxArraySum + alist[i]
    if maxArraySum < 0:
      maxArraySum = 0
    elif maxSum < maxArraySum:
      maxSum = maxArraySum
  return maxSum

array = [5, -4, 1, 3, 4]
print(maxSubArray(array))
