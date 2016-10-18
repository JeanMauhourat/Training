# AXA data scientist training.
# Training session : 8th to 10th of November 2016.
# Trainee : Jean Mauhourat.
#
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
#
# Pre-work - Step 1.
#
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
#
# Exercice 1.
#
# Source : https://nbviewer.jupyter.org/github/tarikd/exo_python/blob/master/basic_list_exercices.ipynb
# Theme : List manipulation.
#
# --------------------------------------------------------------------------------------------------------
#
# A. match_ends
#
# Given a list of strings, return the count of the number of strings where the string length is 2 or more 
#  and the first and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
#
def match_ends(words):
    n=0
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            n+=1
    return n
#
# --------------------------------------------------------------------------------------------------------
#
# B. front_x
#
# Given a list of strings, return a list with the strings in sorted order,
#  except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them before combining them.
#
def front_x(words):
    a=[]
    b=[]
    for word in words:
        if word[0]=='x': a.append(word)
        else: b.append(word)
    a=sorted(a)
    b=sorted(b)
    return a+b
#
# --------------------------------------------------------------------------------------------------------
#
# C. sort_last
#
# Given a list of non-empty tuples, return a list sorted
#  in increasing order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
#
def sort_last(tuples):
    def Last(t): # This local function returns the last elemnent of a tuple.
        return t[-1]
    return sorted(tuples,key=Last)
#
# --------------------------------------------------------------------------------------------------------
#
# Simple provided test() function used in main() to print
#  what each function returns vs. what it's supposed to return.
#
def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)
#
# Calls the above functions with interesting inputs.
#
def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)
#
    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
#   
    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
#
# We call the main function.
#
main() # Displays "OK" everywhere : OK.
#
# --------------------------------------------------------------------------------------------------------
#
# D. remove_adjacent
#
# Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element,
#  so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.
#
def remove_adjacent(nums):
    k=0
    while k<len(nums)-1:
        if nums[k+1]==nums[k]: del nums[k+1]
        else: k+=1
    return nums
#
# --------------------------------------------------------------------------------------------------------
#   
# E. linear_merge
#
# Given two lists sorted in increasing order,
#  create and return a merged list of all the elements in sorted order.
# You may modify the passed in lists. Ideally, the solution should work in "linear" time,
#  making a single pass of both lists.
#
def linear_merge(list1, list2):
    l1=len(list1)
    l2=len(list2)
    k1=0
    k2=0
    ListMerge=[]
    while k1<l1 or k2<l2:
        if k1==l1 and k2<l2:
            ListMerge.append(list2[k2])
            k2+=1        
        elif k2==l2 and k1<l1:
            ListMerge.append(list1[k1])
            k1+=1   
        elif list1[k1]<list2[k2]:
            ListMerge.append(list1[k1])
            k1+=1   
        else:
            ListMerge.append(list2[k2])
            k2+=1   
    return ListMerge
#
# --------------------------------------------------------------------------------------------------------
#  
# Calls the above functions with interesting inputs.
#
def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])
#
    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])
#
# We call the main function.
#
main() # Displays "OK" everywhere : OK.

    

