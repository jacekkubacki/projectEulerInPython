#!/usr/bin/env python3

# Prize Strings
# Problem 191
#
# A particular school offers cash rewards to children with good attendance and punctuality.
# If they are absent for three consecutive days or late on more than one occasion then they forfeit their prize.
#
# During an n-day period a trinary string is formed for each child consisting of L's (late), O's (on time), and A's (absent).

# Although there are eighty-one trinary strings for a 4-day period that can be formed, exactly forty-three strings would lead to a prize:
# OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
# OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
# AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
# AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
# LAOO LAOA LAAO
#
# How many "prize" strings exist over a 30-day period?

n_days = 30

# dictionary to count favorable cases
# the tuple (A , L) is:
# A - current consecutive absences
# L - total number of times being late
# the initial state is: no current consecutive absences (A = 0), never been late (L = 0) -> cases[(0, 1)] = 1
cases = {(0, 0): 1,
         (1, 0): 0,
         (2, 0): 0,
         (0, 1): 0,
         (1, 1): 0,
         (2, 1): 0}

# for every iteration
# the number of prize winning cases will be calculated using 'cases' dictionary and stored in a temporary variables
# and then the dictionary will be updated
for day in range(n_days):
    # ON TIME
    # being on time sets A to 0 and preserves L:
    # cases[(0, 0)] + cases[(1, 0)] + cases[(2, 0)] -> case[(0, 0)], temporarily stored in on_time_0_0
    # cases[(0, 1)] + cases[(1, 1)] + cases[(2, 1)] -> case[(0, 1)], temporarily stored in on_time_0_1
    on_time_0_0 = cases[(0, 0)] + cases[(1, 0)] + cases[(2, 0)]
    on_time_0_1 = cases[(0, 1)] + cases[(1, 1)] + cases[(2, 1)]
    # late
    # being late sets A to 0 and adds 1 to L if L == 0
    # if L is 1 then this is the second time being late - no prize
    late_0_1 = cases[(0, 0)] + cases[(1, 0)] + cases[(2, 0)]
    # absence
    # being absent adds 1 to A if A < 2 and preserves L
    # if A = 2 then this is the third consecutive absence - no prize
    absence_1_0 = cases[(0, 0)]
    absence_2_0 = cases[(1, 0)]
    absence_1_1 = cases[(0, 1)]
    absence_2_1 = cases[(1, 1)]

    # update the dictionary
    cases[(0, 0)] = on_time_0_0
    cases[(1, 0)] = absence_1_0
    cases[(2, 0)] = absence_2_0
    cases[(0, 1)] = on_time_0_1 + late_0_1
    cases[(1, 1)] = absence_1_1
    cases[(2, 1)] = absence_2_1

print ("Result:", sum(cases.values()))




