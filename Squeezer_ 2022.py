#   SQUEEZER    A Gambling Game  FOR AMUSEMENT ONLY
#   PG  2022   just a lil Python programming practice
#   Linear version. 1 Game loop, no functions. EZ variable names and maths
#
# ------------------------------------------------------Intro

print("   ")
print("             SQUEEZER   A Gambling Game  -  FOR AMUSEMENT ONLY ")
print("   ")
print("        TWO RANDOM numbers between 1 and 100 appear.")
print("")
print("        You are asked to bet, up to your balance (open 1000)")
print("      that a THIRD Random number will be inbetween them.")
print("      If you're right you win your bet and it adds to your balance.")
print("      Watch for surprises. Like if you hit 1, the first number,")
print("      second number or 100 ")
print("      Built in Loan Shark. Bonuses for risky bets.")
print("      To quit the game and keep winnings - bet 99999.")
print("      Game ends with zero balance.")

# --------------------------------------------------------- Setup

import random
import pickle

myOpenBalance = 1000


myGainsLosses = 0
myCurBalance = myOpenBalance
myGainsLosses = myCurBalance - myOpenBalance
totalWins = 0
totalLoses = 0
totalBets = 0
HighestBalance = 1000
oldBalance = 0
spacer = 66
gameKey = random.randint(1,100)
round=0
interestRate = 1
interestCharges = 0
totalInterest = 0
loanBalance = 0
cheapBets = 0
bigBets = 0
theSun = 1
shines =0

print("           GameKey    ",  gameKey)
print("   ")

# ------------------------------------------------------------------- Gameplay
#  MAIN GAME LOOP STARTS HERE with while loop

while theSun > shines:
      
    round=round+1
    
    if round == 10:
        print("                Ten rounds BONUS 101      ")
        myCurBalance = myCurBalance + 101

    if round == 20:
        print("                20 rounds BONUS 202      ")
        myCurBalance = myCurBalance + 202
        
    if round == 30:
        print("                30 rounds BONUS 303      ")
        myCurBalance = myCurBalance + 303

    if round == 40:
        print("                40 rounds BONUS 404      ")
        myCurBalance = myCurBalance + 404

    if round == 50:
        print("                50 rounds BONUS 505      ")
        myCurBalance = myCurBalance + 505   

        
        
    print("   ")    
    print(" -----------------------------------------------------------------------  ")
    print(        " LETS PLAY   --- ROUND  " ,round)
    print('')
     
    firstNum = random.randint(1,100)
    secondNum= random.randint(1,100)

    print(" CURRENT BAL      ",myCurBalance, "   Game Gains or LOSS-       ", myGainsLosses," Bets ",totalBets,)
    print(" Winnings   ",totalWins,"   Losses       ",totalLoses, "  Highest Balance ", HighestBalance)
    if loanBalance > 1:
        print(" Loan Balance ",loanBalance," Interest Rate ",interestRate," Interest Charged ",interestCharges,"Total Int. Paid ",totalInterest)
    
    #('reversing if needed ')
    if secondNum < firstNum:     
        spacer = firstNum
        firstNum = secondNum
        secondNum = spacer
        
    # consecutive numbers problem    
    if secondNum-firstNum <=2:
        secondNum = secondNum +2

    range = secondNum - firstNum          
    print("            *************************************************************   ")
    print("                        FIRST",firstNum,"       SECOND", secondNum, "       RANGE     ",range)
    print("            *************************************************************   ")    
      
        
# -------------BET------------------------------------------------------------------------------

    
    myBet= input( "            How much do you bet  ?    " )

   
    # LOANS 
    if loanBalance > 0:
        print("   ")
        interestCharges = int(interestRate * 1 * loanBalance/1000)
        totalInterest= totalInterest+ interestCharges
        print("")
        print("                   Finances first. Interest Charges = ", interestCharges)
        print("")

    if myBet=="" or int(myBet) < 10:
        myBet = 10
        myBet = int(myBet)
        print("")
        print("               Minimum bet is TEN")            
      
        
    if myBet == 10:
        cheapBets  = cheapBets+1

    if int(myBet) > 10:
        cheapBets  = 0    

    if int(myBet)/myCurBalance > .5:
         print("           Go for it")


    if int(myBet)/myCurBalance == 1:
         print("           Bettin the farm")

    if cheapBets> 5:
         print("" )
         print("    Five Minimum BETS.  Come on -  take a chance on something!!")
     

    if int(myBet) == 99999:
            


        
        print("" )
        print("                     YOU  QUIT WHILE AHEAD")
        print("" )
        print("                ******************  END OF GAME  STATS ***********************")

        if loanBalance > 1:
            print("        Loan Balance ",loanBalance," Interest Rate ",interestRate," Interest Charged ",interestCharges,"Total Int. Paid ",totalInterest)
            print("        Please leave a forwarding address, our LOAN COLLECTORS will be in touch")

        print("" )
        print("                You played " , round , " rounds, started with 1000  ")         
        print("                CURRENT      ",myCurBalance, "   Gains net or LOSS-         ", myGainsLosses," Bets ",totalBets,) 
        print("                Winnings   ",totalWins,"   Losses       ",totalLoses, "  Highest Balance          ", HighestBalance) 
        stop
   
   
  

    if int(myBet) > int(myCurBalance):
        print(" ")
        print("          Nice Try. Your bet is cut back to your balance.")
        print(" ")
        
        myBet = myCurBalance

    totalBets = totalBets + int(myBet)   

    

# ------------------------------------------------------  Evaluate
  
    thirdNum = random.randint(1,100)
    print("                      *****************************     ")
    print("                             THIRD NUMBER   ", thirdNum)
    print("                      *****************************     ")
    print("   ")


# goalpost hit---------------------------------------------------------------------------------------------

    if int(thirdNum) == int(secondNum):
            #if int(thirdNum) > int(firstNum):
                print("")
                print("   ***SPECIAL***** You HIT the GOALpost High side WIN your 3X your bet***")
                print("")
                totalWins = totalWins + int(myBet)* 3
                myCurBalance = myCurBalance + int(myBet)*3 - interestCharges
                if myCurBalance > HighestBalance:
                    HighestBalance = myCurBalance
                myGainsLosses = myCurBalance - myOpenBalance
                
    if int(thirdNum) == int(firstNum):
            #if int(thirdNum) > int(firstNum):
                print("")
                print("       ***SPECIAL***** You HIT the GOALpost LOW side WIN your 2X your bet***")
                print("")
                totalWins = totalWins + int(myBet)* 2
                myCurBalance = myCurBalance + int(myBet)* 2 - interestCharges
                if myCurBalance > HighestBalance:
                    HighestBalance = myCurBalance
                myGainsLosses = myCurBalance - myOpenBalance
            


# endpost hit------------------------------------------------------------------------------------------------
   
    if int(thirdNum) == 1:
            if int(thirdNum) > int(firstNum):
                print("")
                print("   ***SPECIAL***** You HIT 1.House wins HALF your balanceSUSPRNDED4TESTING***")
                print("")
                
                
                oldBalance = myCurBalance

                myCurBalance = int(myCurBalance/3)- interestCharges
                thisLoss = oldBalance - myCurBalance 
                totalLoses = totalLoses - thisLoss
                
               
                
                
    if int(thirdNum) == 100:
            if int(thirdNum) > int(firstNum):
                print("")
                print(" ***SPECIAL***** You HIT 100. House wins a THIRD of your moneSUSPRNDED4TESTINGy***")
                print("")
                oldBalance = myCurBalance

                myCurBalance = int(myCurBalance/3)*2 - interestCharges
                thisLoss = oldBalance - myCurBalance 
                totalLoses = totalLoses - thisLoss
               

#win  ----------------------------------------------------------------------------------------------------------

    if int(thirdNum) < int(secondNum):
        if int(thirdNum) > int(firstNum):
            print("")
            print("                   ******** You WIN your bet*********")
            print("")
            totalWins = totalWins + int(myBet)
            myCurBalance = myCurBalance + int(myBet)- interestCharges
            if myCurBalance > HighestBalance:
                HighestBalance = myCurBalance
            myGainsLosses = myCurBalance - myOpenBalance

    if  myCurBalance > 2000 and loanBalance > 100:
         print("")
         print("                  Claiming  1000 to pay down your loan")
         print("           Your interest Rate drops too, due to credit history")
         print("          You only pay back 1000 once you get to 2000 or if you quit.")
         print("             So that means interest is now ", interestRate, " a bet.  ")
         print("")
         
         myCurBalance = myCurBalance - 1000
         loanBalance = loanBalance   -1000
         interestRate = interestRate -1
 
    # loose

    if int (thirdNum) > int(secondNum):        
            print("                    xxxxxx       YOU LOOSE your bet,  over! xxxxxxxx")
            print("")
            totalLoses = totalLoses + int(myBet)
            myCurBalance = myCurBalance - int(myBet)- interestCharges
            myGainsLosses = myCurBalance - myOpenBalance

    
    if int(thirdNum) < int(firstNum):
            print("")
            print("                        ,,,,,,,,,,You LOOSE your bet, under! ,,,,,,")
            print("")
            
            totalLoses = totalLoses + int(myBet)
            myCurBalance = myCurBalance - int(myBet)- interestCharges
            myGainsLosses = myCurBalance - myOpenBalance       


     # balance low
    if  myCurBalance == 1000:
        print("         Right back where you started from")    


    if  myCurBalance == 600:
        print("         In the hole and going down")
        
    if  myCurBalance == 400:
        print("         Not very lucky today?")
        
    if  myCurBalance == 200:
        print("         Just about done? you're gonna need a loan soon")
        

     #balance high


    if  myCurBalance > 2500 and myCurBalance < 3000:
        print("          Gettin a nice bankroll    ")

    if  myCurBalance > 3500 and myCurBalance < 3800:
        print("          You're cleaning up")

    if  myCurBalance > 5000 and myCurBalance < 6000:
        print("          Bet it all, make some real money")

    if  myCurBalance > 8000: 
        print("          I can't afford you!!")   

  
         
    if myCurBalance <= 0 : 
        print("                          You've gone Broke.   Busted")
        print("")
        print("              ******************  END OF GAME  STATS ***********************")

        print("               You played " , round , " rounds, started with 1000  ")         
        print("               CURRENT      ",myCurBalance, "   Gains or LOSS-            ", myGainsLosses," Bets ",totalBets,) 
        print("               Winnings   ",totalWins,"   Losses     ",totalLoses, "  Highest Balance          ", HighestBalance)
    

       
        print("              ******************  END OF GAME ***********************")
        print("")
        print("                You've gone Broke? So sad. No problem, I'll give you a new loan?")    
        print("                How about a 1000 at a good interest rate per loan a bet, no problem.   ")
        print("")
        
        myCurBalance  = myCurBalance + 1000
        
        interestRate = interestRate +1
        
        loanBalance = loanBalance +1000
        
        print("                So that means interest is now ", interestRate, " a bet.  ")
        print("                You only pay back 1000 once you get to 2000 or if you quit.")
              
