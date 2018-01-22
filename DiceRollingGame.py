import random #import module

#min and max for dice
min = 1 
max = 6

roll_again = "yes"  #sets up while statement to run first time

#rolls dice and asks if want to roll again
while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
    print (random.randint(min, max))
    
    roll_again = input("Roll the dices again?")

