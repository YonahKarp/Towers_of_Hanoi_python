
##Function definitions##
#----------------------#

def display():
  for i in range(len(twr1)):
    print (" " + (" " if twr1[i] == 0 else str(twr1[i])) +\
    "   "  + (" " if twr2[i] == 0 else str(twr2[i])) +\
    "   " + (" " if twr3[i] == 0 else str(twr3[i])))
    
  print ("--- --- ---")
  print (" A   B   C ")

    
def getInput():
  x = input();
  
  if x == 'ab':
    move(twr1,twr2)
  elif x == 'ac':
    move(twr1,twr3)
  elif x == 'ba':
   move(twr2,twr1)
  elif x == 'bc':
    move(twr2,twr3)
  elif x == 'ca':
    move(twr3,twr1)
  elif x == 'cb':
    move(twr3,twr2)
  elif x == 'solve':
    setTowers()
    solve(disks, twr1,twr2,twr3, "A", "B", "C")
    setTowers()
    print("\nnow you try!")
  else:
    print("invalid input: format should be \"ab\" \(means from A to B\)")
   

def move(twrA, twrB):

  position = -1
  top = len(twrB)-1

  for i in range(len(twrA)):
    if(twrA[i]!=0):
      position = i
      break
    
  if(position == -1):
    print("No disks left")
    return

  for i in range(len(twrB)-1, -1, -1):
    top = i;
    if(twrB[i] == 0):
      break
    
  if(twrB[len(twrB) - 1]!=0 and twrB[top+1] <= twrA[position]):
    print("illegal move")
    
  else:
    twrB[top] = twrA[position]
    twrA[position] = 0

    
def solve(n, frm, using, to, fromName, usingName, toName):
  if (n == 1):
    move(frm, to)
    display()
    print ("disk moved form {x} to {y}".format(x=fromName, y = toName))
    input("press enter to continue")
  else:
    solve(n - 1, frm, to, using, fromName, toName, usingName)
    move(frm, to)
    display()
    print ("disk moved form {x} to {y}".format(x=fromName, y = toName))
    input("press enter to continue")
    solve(n - 1, using, frm, to, usingName, fromName, toName)
  

def setTowers(): 
  for i in range(0, disks):
    twr1[i] = i+1
    twr2[i] = 0
    twr3[i] = 0

  

##Start Program##
#---------------#

disks = 0
totalMoves = 0

while(disks < 1):
  disks = int(input("Enter the number of disks you would like to use"))
  
  
twr1 = [0]*disks
twr2 = [0]*disks
twr3 = [0]*disks

setTowers()

print ("Enter a move. format should be \"FromTo\" for example \"ab\" means from A to B")

while(twr3[0] == 0):
  display()
  getInput()
  totalMoves += 1
  
display();
print ("YAY! You Win! Your total moves were ",totalMoves);

