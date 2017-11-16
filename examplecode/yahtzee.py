import random
from test import testEqual

# The roll_dice function simulates the rolling of the dice. It
# creates a 2 dimensional list: each column is a die and each
# row is a throw. The function generates random numbers 1-6
# and puts them in the list.
def roll_dice(num_dice, num_rolls):

    # create a two-dimensional (num_dice by num_rolls) of zeros
    double_list = [[0 for i in range(num_dice)] for j in range(num_rolls)]

    # loop through each row and column, filling it with a random roll
    for roll in range(0, len(double_list)):
      for die in range(0, len(double_list[roll])):
          double_list[roll][die] = (int)(random.random()*6 + 1)

    return double_list


# This function takes a 2D list (which can be generated by roll_dice)
# and sums the value of all the dice in each row. It returns a 1
# dimensional list with the sum of each throw.
# Example:
# double_list: [[1, 5, 6],[2, 3, 1],[1, 3, 3]]
# sum_of_roll should return: [12, 6, 7]



#def sum_of_roll(double_list):
    # Your code here
#    total_list =[]
#    for i in double_list:
#        total = sum(i)
#        total_list.append(total)
#        print(i)
#    print(total_list)
#    return total_list

def sum_of_roll(double_list):
   
    num_of_dice = len(double_list)
    total_of_list = []
    
    for x in range(0, num_of_dice):
        
        total =0
        for y in range(len(double_list[x])):
            total = total + double_list[x][y]
        total_of_list.append(total)
    return total_of_list
                    
    
    
   
            


# Bonus function! Takes a 2D list and returns
# the number of times a person rolls Yahtzee (all dice have
# the same value). Hint: you may want to create a helper
# function that takes individual rows of the list.

def test_equal(input_list):
    for i in range(len(input_list)-1):
        if input_list[i] != input_list[i+1]:
            return False
    return True


def yahtzee(double_list):
    # Bonus: your code here
    counter = 0
    for i in range(0,len(double_list)):
        if test_equal(double_list[i]) == True:
            counter =+ 1
            
    return counter
    
    


# To play, yo'd do something like this
# dice = input("How many dice?")
# rolls = input("What is the number of rolls?")
# list = roll_dice(dice, rolls)
# print("Sum of roll:", sum_of_roll(list))

print("Testing sum_of_roll...")
testEqual(sum_of_roll([[4, 5, 2],[6,2,1],[4,4,4]]), [11, 9, 12])
testEqual(sum_of_roll([[3, 4, 6],[2,6,1],[3,4,3]]), [13, 9, 10])
print("Testing yahtzee...")
testEqual(yahtzee([[4, 5, 2],[6,2,1],[4,4,4]]), 1)
testEqual(yahtzee([[3, 4, 6],[2,6,1],[3,4,3]]), 0)
