from adjacent_digits import count_non_adjacent_digits
__author__ = 'julz'

# print count_non_adjacent_digits(4)
# 4
# print count_non_adjacent_digits(5)
# 5
# print count_non_adjacent_digits(10)
# 8

for i in range(0,21):
    print '%s : %s' %(i, count_non_adjacent_digits(i))
#   0 : 1
#   1 : 2
#   2 : 3
#   3 : 3
#   4 : 4
#   5 : 5
#   6 : 5
#   7 : 5
#   8 : 6
#   9 : 7
#   10 : 8
#   11 : 8
#   12 : 8
#   13 : 8
#   14 : 8
#   15 : 8
#   16 : 9
#   17 : 10
#   18 : 11
#   19 : 11
#   20 : 12