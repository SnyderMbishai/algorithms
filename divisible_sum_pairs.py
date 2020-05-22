"""
You are given an array of n integers, ar=[ar[0],ar[1]],...,ar[n-1] , and a positive integer, k . Find and print the number of (i,j)  pairs
 where i < j and ar[i] + ar[j] is divisible by k .

For example, ar=[1,2,3,4,5,6] and k=5. Our three pairs meeting the criteria are [1,4],[2,3] and [4,6].

Function Description

Complete the divisibleSumPairs function in the editor below. It should return the integer count of pairs meeting the criteria.

divisibleSumPairs has the following parameter(s):

n: the integer length of array 
ar: an array of integers
k: the integer to divide the pair sum by

Input Format

The first line contains 2 space-separated integers, n and k.
The second line contains n space-separated integers describing the values of ar[ar[0],ar[1],...,ar[n-1]].

Constraints

2 <_ n <_ 100
1 <_ k <_ 100
1 <_ ar[i] <_ 100

Output Format

Print the number of (i,j) pairs where i<j and a[i] + a[j] is evenly divisible by k.
"""

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):  
    count = 0
    for a,b in enumerate(ar):
        for c in ar[a+1:]:
            if (b+c) % k == 0:
                count += 1
    return count

if __name__ == '__main__':
    n = 6
    k = 5
    ar = [1,2,3,4,5,6]
    print(divisibleSumPairs(n, k, ar))

