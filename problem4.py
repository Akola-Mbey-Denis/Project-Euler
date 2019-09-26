def isPalindrome(num):
    number=str(num)
    reversed=""
    for i in range(len(number)-1,-1,-1) :
        reversed+=number[i]
    return number==reversed

def palindrome_multiple():
    palindrome=-1
    for i in range(999,99,-1):
        for j in range(i,99,-1):

            if isPalindrome(i*j) and i*j>palindrome:
                palindrome=i*j
    return palindrome  





if __name__=="__main__":
    print(isPalindrome(99999)) 
    print(palindrome_multiple())     