#
# Given the participants' score sheet for your University Sports Day, you are required
# to find the runner-up score. You are given n scores.
# Store them in a list and find the score of the runner-up.
#
# Input Format
#
# The second line contains an array  A[] of n integers each separated by a space.
#
# Constraints
#
# -100 <= A[i] <= 100
#
# Output Format
#
# Print the runner-up score.
#
# Sample Input 0
#
#
# 2 3 6 6 5
# Sample Output 0
#
# 5
# Explanation 0
#
# Given list is [2,3,2,5,6,6,5]. The maximum score is 6, second maximum is 5.
# Hence, we print 5 as the runner-up score.
#
if __name__ == '__main__':
    n = input()
    arr = list(map(int, n.split()))


    #print(sorted(list(set(arr)))[-2])
    Arr = set(arr)
    arr_list = list(Arr)
    Sort = sorted(arr_list)[-2]
    print(Sort)