# problem: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true
# - TIME: O(n)
# - SPACE: O(n)
#   - ***ORACLE OCI PRACTICE HACKERRANK *** typical solution using an extra array of size n-1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    
    arr.sort()                      # first sort the array
    
    absDif = []
    num1 = arr[0]
    for i in range(1, len(arr)):    # next, calculate the absolute differences
        num2 = arr[i] 
        absDiff.append(num1+num2*-1)
        num1 = num2
        
    result = 0
    for i in range(len(absDif)):    # lastly, add them up and return the result
        result+=absDif[i]
    
    return result

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
