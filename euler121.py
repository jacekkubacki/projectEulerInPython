#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# the above line allows '£' to be in the source code without PyCharm complaining about it
'''
Disc game prize fund
Problem 121

A bag contains one red disc and one blue disc.
In a game of chance a player takes a disc at random and its colour is noted.
After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.

The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.
If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss.
Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given the player actually wins £9.

Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.
'''

'''
Solution:

For the game to be fair the expected value must be 0.
We are looking for a game with expected value <= 0.

eX <= p1*(x1-1) + p2*x2

where
p1 : probability of winning, p1>0
x1 : prize, we subtract £1 as the player must pay to win the prize
p2 : probability of losing, p2>0
x2 : -1, player pays £1 to play

0 <= p1*(x1-1) - p2
x1 <= p2/p1 + 1

The answer would be the integer part of x1, as int(x1) <= x1 for x1>=0.

Because
p1 = casesFavorable / allCases
and
p2 = 1 - p1 = 1 - casesFavorable / allCases = (allCases - casesFavorable) / allCases

then
x1 <= p2/p1 + 1 = (allCases - casesFavorable) / allCases  + 1

It the first round we have 2 disk to choose from, in the second there are 3 disks and so on.
In the Nth round there are N+1 disks to choose from.
That gives us allCases = 2 * 3 * ... * N * (N+1) = (N+1)!

casesFavorable will be found by brute force, see below.
'''

from math import factorial

rounds = 15
casesFavorable = 0
allCases = factorial (rounds + 1)

# to go through all the cases we will check all the n-digit binary numbers (n = rounds)
# and treat 0 as a red disk and 1 as a blue disk
# the binary number with more then a half of 1s (blue disks) is a favourable case 
for i in range (0, pow(2,rounds)):
    # convert to binary, remove '0b' and add leading zeros
    s = bin(i)[2:].zfill(rounds)
    
    if s.count('1') > len(s) // 2:
        # it is a win! but in how many ways can this happen?
        p = 1

        # go through the number and multiply... 
        for x in range (0, len(s)):
            if s[x] == '0':
                #...by (x+1), because there are x+1 red disks in round x+1
                p *= (x + 1) 
            #... or by 1 (no change), becuse there is only one blue disk in round x+1
            
        casesFavorable += p
        
print ("Result:", int((allCases - casesFavorable) / casesFavorable + 1))
