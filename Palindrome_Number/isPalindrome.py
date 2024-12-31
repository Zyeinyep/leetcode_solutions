class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        l = len(x)
        if l == 0:
            return False
        if x[0] == '-' or x[0] =='+':
            return False
        
        if l % 2 == 0:
            arr= x[0:l/2]
            print(arr)
            arr2 = x[l/2:]
            print(arr2)
            if list(arr )== list(reversed(arr2)):
                return True
            else:
                return False

        else:
           
            arr= x[0:(l-1)/2]
            print(arr)
            arr2 = x[(l+1)/2:]
            print(arr2)
            print(list(reversed(arr2)), list(arr))
            if list(arr )== list(reversed(arr2)):
                return True
            else:
                return False

        
