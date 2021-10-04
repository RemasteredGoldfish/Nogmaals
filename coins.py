# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

#opdracht is dat je in de comments laten zien wat het betekent en nieuwe vaule in zetten

toPay = int(float(input('Amount to pay: '))* 100) #The amount you have to pay (float = 'example' 2.54)
paid = int(float(input('Paid amount: ')) * 100) #The amount you already paid (float = 'example' 2.54)
change = paid - toPay #The amount you already paid - the amount you have to pay = the change

if change > 0: #If change is bigger then 0
  coinValue = 50 #CoinValue is equal to 50
  
  while change > 0 and coinValue > 0:
    nrCoins = change // coinValue #coinValue // (floor division and round it of to a whole number) change = nrCoins 

    if nrCoins > 0: #if nrCoins is bigger then 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #It prints the nrCoins and the Coinvalue with some text
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #It tells u how many coins of the coinvalue did you return
      change -= nrCoinsReturned * coinValue #coinvalue times nrCOinsReturn = changee

# comment on code below:
      coinValue = 500
    elif coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:     #if convalue == 50 cent
      coinValue = 20
    elif coinValue == 20:     #if convalue == 20 cent
      coinValue = 10
    elif coinValue == 10:     #if convalue == 10 cent
      coinValue = 5
    elif coinValue == 5:      #if convalue == 5 cent
      coinValue = 2
    elif coinValue == 2:      #if convalue == 2 cent
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #if change is bigger then 0
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')