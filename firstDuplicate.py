from collections import defaultdict

def firstDuplicate(a):
    # # brute force O(n^2)
    # n = len(a)
    # repeat_indx = n
    # ans = -1
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if a[i] == a[j]:
    #             if j < repeat_indx:
    #                 ans = a[i]
    #                 repeat_indx = j
    #             break
    # return ans
    
#     # More efficient O(n) - Hash table
#     n = len(a)
#     d = {}
    
#     for i,num in enumerate(a):
#         if num not in d:
#             d[num] = 0
#         elif d[num] == 0:
#             d[num] = i
    
#     ans = -1
#     smallest_indx = n
#     for num in d:
#         if 0 < d[num] < smallest_indx:
#             smallest_indx = d[num]
#             ans = num
            
    # More efficient O(n) - array
    for x in a:
        a[abs(x) - 1] *= -1
        if a[abs(x) - 1] > 0:
            return abs(x)
    return -1
