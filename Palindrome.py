def PalindromeRecursion(string,start,end):

    
    if(start>=end):
        return 1
    if string[start]!=string[end]:
        return 0
    
    return PalindromeRecursion(string,start+1,end-1)

string=input("enter the string: ")
print(PalindromeRecursion(string,0,len(string)-1))