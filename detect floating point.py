 # Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
number=int(input( ))

for i in range(0,number):
 string=input()
 try: 
  if len(string)>1:
    new_string= float(string)
  
    print(True)
  else:
    print(False)
 except:
   print(False) 

