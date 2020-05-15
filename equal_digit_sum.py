"""
Numbers With Equal Digit Sum
Given array A consisting of N intergers, 
return maximum sum of two numbers whose digits add up to an equal sum. 
Otherwise, return -1
"""

def digits_sum(n):
    """ calculates sum of integer digits """
    sum_of_digits = 0
    while n:
        sum_of_digits += n % 10
        n //= 10
    return sum_of_digits

def equal_digit_sum(A):
    """ finds maximum sum of intergers with equal sum of digits """
    pairs = {} #holds sum and interger pairs
    res = -1 #final sum or -1 if none
    for i in A:
        sum_i = digits_sum(i) #calculate sum
        if sum_i in pairs:
            second_val = pairs[sum_i]
            res = max(res, i+second_val)
            pairs[sum_i] = max(i, second_val)
        else:
            pairs[sum_i] = i
    print(res)
    return res
        

equal_digit_sum([51, 71, 17, 42])
equal_digit_sum([42, 33, 60])
equal_digit_sum([51,32,43])
