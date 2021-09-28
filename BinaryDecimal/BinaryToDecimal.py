
#================= by  AMANUEL ATNAFU =====================================

userInput=(input("enter an upto 5 bit number: "))
i,g,l= 0,0,0
v = len(userInput)
let=1
for g in userInput:
   z=let*int(g)
   let*=2
   l+=z
while i < len(userInput):
  if userInput[i]=='0' or userInput[i]=='1':
      check=True
      i+=1
  else:
      check=False
      break
if check==True  and v<=5:
    print("the value in decimal is: ",l)
elif check==True  and v>=5:
    print("over 5 digit")
else:
 print("not a valid binary number")



#================================ END ==================================