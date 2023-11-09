#function that takes a string and returns the number of unique characters in it
#we put input string
string=input("enter a string:")
unique_character="!@#$%^&*()<>?/{}[]|"
count=0
for i in string:
     if i in unique_character: 
          count=count+1 #string have unigue characters count will be increse
print("number of unique charecters:",count)        