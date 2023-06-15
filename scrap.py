#!/usr/bin/env python3
import random


#dice1 = x
#dice2 = y
#total = z
#jackpot = j
#tally = a


j = 0
a = 0
x = 0
y = 0
z = 0
while j < 3:
     x = random.randint(1, 25)
     y = random.randint(1, 25)
     z = x + y
     a += 1
     print("Dice one got {}, dice two got {}! That makes {}! Current roll is: {}".format(x, y, z, a))
     if a == 500000:
          print("Too many tries!")
          break
     if z == 7:
          j += 1
     else:
          j = 0
if j == 3:
     print("Three 7's, jackpot in {} rolls!".format(a))
