#return new string all the vowels removed
#voeels"aeiouAEIOU"
#using for loop and if condition
string=input("enter a string:")
vowels="aeiouAEIOU"
for i in string:
 if i not in vowels:
  print(i,end="")