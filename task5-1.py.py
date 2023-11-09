# calculate the total number of vowels and count of each individual vowel
#vowels "aeiouAEIOU"
string="Guvi Geeks Private Limited" 
t_count=0
a_count=0
e_count=0
i_count=0
o_count=0
u_count=0
A_count=0
E_count=0
I_count=0
O_count=0
U_count=0
vowels="aeiouAEIOU"  
for i in string:
  if(i in vowels):
   t_count=t_count+1
for i in string:
  if(i in "a"):
    a_count=a_count+1
  elif(i in "e"):
    e_count=e_count+1
  elif(i in "i"):
    i_count=i_count+1 
  elif(i in "o"):
    o_count=o_count+1
  elif(i in "u"):
    u_count=u_count+1 
  elif(i in "A"):
    A_count=A_count+1
  elif(i in "E"):
    E_count=E_count+1 
  elif(i in "I"):
    I_count=I_count+1
  elif(i in "O"):
    O_count=O_count+1  
  elif(i in "U"):
    U_count=U_count+ 1   
print("TOTAL NUMBER OF VOWELS:",t_count)                   
print("vowel-a-",a_count)   
print("vowel-e-",e_count)  
print("vowel-i-",i_count)  
print("vowel-o-",o_count)  
print("vowel-u-",u_count)  
print("vowel-A-",A_count)  
print("vowel-E-",E_count)  
print("vowel-I-",I_count)  
print("vowel-O-",O_count)  
print("vowel-U-",U_count)  




