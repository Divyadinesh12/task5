#function to check if two strings are anagram each other or not
#anagram of a string is another string that contains the same character
string1=input("enter string:")
string2=input("enter string:")
#the sorted string are checked
#sorted(function returns a sorted list from the items
if(sorted(string1)==sorted(string2)):
  print("true")
else:
  print("else")