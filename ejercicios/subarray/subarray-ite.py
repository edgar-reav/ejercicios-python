from sys import maxsize

def maxSubArraySum(a,size):
      
    max_so_far = -maxsize - 1
    max_ending_here = 0
      
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far
  
# Driver function to check the above function
arr = [-7,6,-5,-2,8,-1,2,-4,-3,-6]
arr2 = [-5, 2, 10, -7, 4, -2, 1, 0]
print("Maximum contiguous sum is", maxSubArraySum(arr2,len(arr2))) 