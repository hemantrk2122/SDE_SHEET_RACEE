def search_in_2d_array(mat, n, x):
    #Given a row and column wise sorted array, find a value x in it using binary search.
    low = 0
    high = n * n - 1      # last index in 2d grid
    while low <= high:
        mid = (low + high) // 2
        row = mid // n        # By pattern, we found this relation. Just compare row & column indexesin grid with the mid value.
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
   
