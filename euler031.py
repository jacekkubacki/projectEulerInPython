#!/usr/local/bin/python3
'''
Coin sums
Problem 31

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

'''
Solution:
The idea is to build all the possible lists of coins in a descending value order.
We start with list containig the sublists with one coin of each type.
Then we parse through the list and:
- remove the sublist if it ends with 1 - it means that the sublist would end with one or more 1p coins
- remove the sublist if the sum of the coins equals 200
- replace current sublist with new sublists created by adding a coin (same or smaller value) to the current sublist
Repeat the process until the list is empty.
'''

result = 0
total = 200
coins = [200,100,50,20,10,5,2,1]
current = [[c] for c in coins]

while len(current)>0:
    tmp = [] # to build _current_ list for the next iteration

    for c in current:

        # solution found: coins sum up to 200
        if sum(c) == total:
            result += 1
            continue

        # solution found: only 1p coin(s) left
        if c[-1] == 1:
            result += 1
            continue

        # find the position of the last coin in _coins_
        # to add only the coins of same or smaller value
        i = coins.index(c[-1])
        for coin in coins[i:]:
            if coin + sum(c) <= total:
                # create and add new sublists to _tmp_
                t = list(c)
                t.append(coin)
                tmp.append(t)
    # work with _tmp_ list in the next iteration
    current = tmp      
        
print ("Result: ", result)

# I can't be bothered to write a nice function
