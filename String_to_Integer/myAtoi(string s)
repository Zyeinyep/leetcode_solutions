class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_int = 2**31 - 1
        min_int = -2**31
        mylist = []
        empty = 0
        zeros = 0
        minus = 0
        is_num = 0
       
        print(len(s))
        
        for index, char in enumerate(s):

            if not char.isdigit():
                if is_num == 1:
                    break
               
                if index -1 > -1 and s[index-1]== '0':
                    return 0
                if char == " ":
                    empty += 1
                    if index -1 >-1 and s[index-1].isdigit() and index +1 < len(s) and s[index+1].isdigit():
                        return 0
                   
                elif (char == "-" or char == "+" )and index - empty == 0 :
                    if index+1 < len(s) and not s[index+1].isdigit():
                        return 0
                    
                    print(char,index, empty)
                    minus += 1
                    mylist.append(char)

                else:
                    break
              
            else:
                is_num = 1
              
                if char == '0':
                    zeros += 1
                    if index -1 > -1 and s[index-1].isdigit():
                        mylist.append(char)

                else:
                    if index - (zeros + minus + empty) == 0 and (zeros != 0 or minus != 0 or empty !=0) :
                      
                        mylist.append(char)
                        
                        

                    else:
                       
                        mylist.append(char)
                       
        print("mmm", mylist)
        if len(mylist) == 0 or (len(mylist) == 1 and (mylist[0] == '-' or mylist[0] == '+')):
            return 0
        digit = int("".join(mylist))
        # print(digit,type(digit))
        if digit > max_int:
            return max_int
        elif digit < min_int:
            return min_int
        return digit





                
             
            

        
