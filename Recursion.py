""" 
Recusrsion is based  on the concept of PMI. Steps for any PMI problem:
1) Solve it for smallest value. (k = 1 step for PMI)
2) Keep faith that it will work for some smaller value. (Assume the f(k) is true)
3)Solve it for larger value using your faith. (Prove f(k+1) is true)

In recursion, steps are:
1) solve it for smallest value. ie, write base case.
2) have faith that it will work for smaller values. ie. write calls
3) match faith with expectation.
"""

#########################################################################

def printDecreasing(n):
    # write your code here
    if n < 0:     # step 2: smallest case
        return
    print(n)         # match faith with expectation.we have to print, hence this line.
    printDecreasing(n -1)        # step 1: write faith
n = int(input())
printDecreasing(n)
