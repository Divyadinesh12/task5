#returns most frequent character 
#naive method
#initialize string
string=input("enter string:")
all_freq={}
for i in string:
    if i in all_freq:
      all_freq [i]=all_freq[i]+1
    else:
       all_freq[i]=1
result=max(all_freq,key=all_freq.get)
print(result)  #print result     