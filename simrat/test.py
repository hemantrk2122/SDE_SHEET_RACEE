# Permutation Sequence
fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
def getPermutationHelper(arr,k,s = ""):
    if len(arr) == 0:
        return s
    else:
        n = len(arr)
        inx = k//fact[n-1]
        return getPermutationHelper(arr[:inx]+arr[inx+1:],k%fact[n-1],s+arr[inx])
        

n = 5
k = 1
print(getPermutationHelper([str(i) for i in range(1,n+1)],k-1,''))



