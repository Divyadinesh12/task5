#function that takes a sting and returns true if it is a palindrome otherwise false
#palindrome is word or number that reads the same backwards as forwards
#such as madam,racecar
palindrome_string=(input("enter string:"))
#we get the reverse of the input string using slice operator string[::-1]
if(palindrome_string==palindrome_string[::-1]):
    print("true")
else:
    print("false") 