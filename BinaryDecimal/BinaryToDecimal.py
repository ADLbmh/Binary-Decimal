
#================= by  ADlbmh =====================================

userInput=(input("enter an upto 5 bit number: "))
i,g,l= 0,0,0
v = len(userInput)
let=1
while i < len(userInput):
  if userInput[i]=='0' or userInput[i]=='1':
      check=True
      i+=1
  else:
      check=False
      break
if check==True:
   l=int(userInput,2)
    print("the value in decimal is: ",l)
else:
 print("not a valid binary number")



#================================ END ==================================
