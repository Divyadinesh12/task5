#create a pyramid of numbers
#range1-20
rows=21 
space=2*rows-2     #it is used for number of space
for i in range(1,rows):
  for j in range(1,space):
      print(end=" ")
  space=space-1    #decrement space after each iteration
  for j in range(1,i+1):
      print(j,end=" ")
  print("")    