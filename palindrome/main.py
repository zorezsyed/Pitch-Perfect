inputWord = input("Please enter a word so we could find out if it is a palindrome: ")

def isPalindrome(inWord):
    for i in range(int(len(inWord)/2)):
        if inWord[i] != inWord[len(inWord)-1-i]:
            print("It isn't a palindrome.")
            return False
    print("It is a palindrome.")
    return True

isPalindrome(inputWord)



 
