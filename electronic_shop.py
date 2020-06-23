"""
Monica wants to buy a keyboard and a USB drive from her favorite electronics store. The store has several models of each. 
Monica wants to spend as much as possible for the 2 items, given her budget.

Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and print the amount of money Monica will spend. 
If she doesn't have enough money to both a keyboard and a USB drive, print -1 instead. She will buy only the two required items.

For example, suppose she has b=60 to spend. Three types of keyboards cost keyboards=[40,50,60]. Two USB drives cost drives=[5,8,12]. 
She could purchase a 40 keyboard + 12 USB drive =52, or a 50 keyboard + 8 USB drive =58. She chooses the latter. She can't buy more than 2 items
so she can't spend exactly 60.

Function Description:

Complete the getMoneySpent function in the editor below. It should return the maximum total price for the two items within Monica's budget, or -1
if she cannot afford both items.

getMoneySpent has the following parameter(s):

keyboards: an array of integers representing keyboard prices
drives: an array of integers representing drive prices
b: the units of currency in Monica's budget

Input Format:

The first line contains three space-separated integers b, n, and m, her budget, the number of keyboard models and the number of USB drive models.
The second line contains n space-separated integers keyboard[i], the prices of each keyboard model.
The third line contains m space-separated integers drives, the prices of the USB drives.

Constraints:
- 1 <= n,m <= 1000
- 1 <= b <= 10^6
- The price of each item is in the inclusive range [1,10^6].

Output Format:

Print a single integer denoting the amount of money Monica will spend. If she doesn't have enough money to buy one keyboard 
and one USB drive, print -1 instead.

LINK: https://www.hackerrank.com/challenges/electronics-shop/problem
"""

# with built-in max
def getMoneySpent(keyboards, drives, b):
    return max([k+d for k in keyboards for d in drives if k+d <= b]+[-1])



# without built-in max
def getMoneySpent1(keyboards, drives, b):
    mx = -1
    for k in keyboards:
        for d in drives:
            s =k+d
            if s <= b and s > mx:
                mx = s           
    return mx

if __name__=='__main__':
    k = [3,1]
    d = [5,2,8]
    b = 10
    print(getMoneySpent(k,d,b))
    print(getMoneySpent1(k,d,b))
