def search_in_2d_array(mat, n, x):
    #Given a row and column wise sorted array, find a value x in it using binary search.
    low = 0
    high = n * n - 1      # last index in 2d grid
    while low <= high:
        mid = (low + high) // 2
        row = mid // n        # By pattern, we found this relation. Just compare row & column indexes in grid with the mid value.
        col = mid % n         # This question teaches us to apply bin. search in a 2d array. Rest of code is simple binary search.
        if mat[row][col] == x:
            print (row)
            print (col)
            return
        if mat[row][col] > x:
            high = mid - 1
        else:
            low = mid + 1
    print('Not Found')
 
####################################################################

def printallpalindrome(st):
  # Print all palindomic substrings. Extract all substrings using 2 for loops, and check for palindrome in each case. 
  for i in range(len(st)):
    s = st[i]           
    for j in range(i + 1, len(st) + 1):   # Note len(st) + 1 here. This is right because in next line, last index will be left out as j is non inclusive
                                          # while taking substrings in python. 
      s = st[i:j]           # Extracting Substring
      if s == s[::-1]:      # checking for palindrome
        print(s)

################################################################
def toggleCase(string): 
    # If char of string is lower convert it to upper and vice versa.  
    res = ''
    for i in range(len(string)):
        if string[i].isupper():
            res += string[i].lower()
        else:
            res += string[i].upper()
    print(res)

###################################################################

def String_compression01(st):
   # Remove all duplicates from a string. String will have same letters contigiously.
   # "wwwwaaadexxxxxx" If this is string, ans should be 'wadex'.
   # If next char is same, start another loop, which will continue untill next char is different. THis is done in the 2nd while loop here.
   # If next char is different, just add next characterto the result string.
    i = 0
    res = ''
    while i < len(st):
        if i < len(st) - 1 and st[i] == st[i + 1]:     # if next char is same, keep iterate and shift i to next different character index.
            j = i              # index for this while loop.
            while j < len(st):      # Keep iterating untill st[j+1] is ot equal to st[i]
                if st[i] == st[j]:     
                    j += 1
                else:
                    break
            res += st[i]      # add to answer string
            i = j - 1   # Update i to next different character index.
        else:
            res += st[i]  # If next char is differet, directly add it to res as it has no duplicates.
        i += 1
    print( res )  

######################################################################################

def removePrimeFromList(al):
    # Remove all primes from a given list. Here catch is list size will change everytime we remove an element. Eg. arr =[12,11,33,4]
    # At idx 2, i = 1. Its prime so we remove it and arr = [12,33,4]. i is updated in every iteration, so i = 2. 33 is skipped.
    # Hence whenever we remove element from arr,  we subtract i by 1.
    def isprime(n):    # Function to check prime
        if n in [0,1,2]:
            return True
        for i in range(2, int(n**(1/2) ) + 1):
            if n % i == 0:
                return False
        return True
    i = 0
    while i < len(al) - 1:        
        if isprime(al[i]):               #If arr[i] is prime,
            al.pop(i)                    # remove that element from list
            i = i - 1                   # reduce i by 1 so that no element is skipped.
        i += 1
    
############################################################

    
