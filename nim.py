stones = 12
while stones >= 0:
  
    user_num = input('Pick a number from 1 to 3: ')
    
    stones = stones - int(user_num)
    print ("The number of objects is now: ",  stones)
while int(user_num)<1 or int(user_num)>3: 

    print ("There are," + stones + " stones left")

if stones == 0:
  print ("You Won!!")
  #break

if stones <= 3:
  com_num = stones

print ("The computer took, ",  com_num,  " stones")

stones = stones - com_num

print ("The number of objects is now: ",  stones)

if stones == 0:
  print ("you Won!!")
  #break


  
