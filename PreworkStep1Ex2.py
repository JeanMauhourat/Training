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
# Exercice 2.
#
# Source : https://nbviewer.jupyter.org/github/tarikd/exo_python/blob/master/basic_string_exercices.ipynb
# Theme : Basic string exercises.
#
# --------------------------------------------------------------------------------------------------------
#
# A. donuts
#
# Given an int count of a number of donuts, return a string of the form 'Number of donuts: ',
#  where  is the number passed in. However, if the count is 10 or more, then use the word 'many'
#  instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5' and donuts(23) returns 'Number of donuts: many'
#
def donuts(count):
    if count>9: s='many'
    else: s=str(count)
    return 'Number of donuts: '+s
#
# --------------------------------------------------------------------------------------------------------   
# 
# B. both_ends
#
# Given a string s, return a string made of the first 2 and the last 2 chars of the original string,
#  so 'spring' yields 'spng'. However, if the string length is less than 2,
#  return instead the empty string.
#
def both_ends(s):
    if len(s)<2 : ss=''
    else: ss=s[:2]+s[-2:]
    return ss
#
# --------------------------------------------------------------------------------------------------------   
# 
# C. fix_start
#
# Given a string s, return a string where all occurences of its first char have been changed to '*',
# except do not change the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s where all instances of stra 
#  have been replaced by strb.
#
def fix_start(s):
    return s[0]+s[1:].replace(s[0],'*')
#
# --------------------------------------------------------------------------------------------------------
# 
# D. mix_up
#
# Given strings a and b, return a single string with a and b separated by a space '<a> <b>',
#  except swap the first 2 chars of each string.
# e.g.
#  'mix', pod' -> 'pox mid'
#  'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
#
def mix_up(a, b):
    return b[:2]+a[2:]+' '+a[:2]+b[2:]
#
# --------------------------------------------------------------------------------------------------------
#   
# Provided simple test() function used in main() to print what each function 
#  returns vs. what it's supposed to return.
#
def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)
#
# Provided main() calls the above functions with interesting inputs,
#  using test() to check if each result is correct or not.
#
def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')
#
    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')
#  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')
#
    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')
#
# We call the main function.
#
main() # Displays everywhere "OK" : OK.
#
# --------------------------------------------------------------------------------------------------------
#
# E. verbing
#
# Given a string, if its length is at least 3, add 'ing' to its end.
# Unless it already ends in 'ing', in which case add 'ly' instead.
# If the string length is less than 3, leave it unchanged. Return the resulting string.
#
def verbing(s):
    if len(s)<3: ss=s
    elif s[-3:]=='ing': ss=s+'ly'
    else: ss=s+'ing'
    return ss
#
# --------------------------------------------------------------------------------------------------------   
#  
# F. not_bad
#
# Given a string, find the first appearance of the substring 'not' and 'bad'.
# If the 'bad' follows the 'not', replace the whole 'not'...'bad' substring 
#  with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields: This dinner is good!
#
def not_bad(s):
    n1=s.find('not')
    n2=s.find('bad')
    if n1<n2: ss=s[:n1]+'good'+s[n2+3:]
    else: ss=s
    return ss
#
# --------------------------------------------------------------------------------------------------------    
#
# G. front_back
#
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b,
#  return a string of the form a-front + b-front + a-back + b-back
#
def front_back(a, b):
    def NbFront(c):
        l=len(c)
        return l//2+l%2
    def Front(c):
        return c[:NbFront(c)]
    def Back(c):
        return c[NbFront(c):]
    return Front(a)+Front(b)+Back(a)+Back(b)
#
def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
#   
    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")
#
    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')
#
# We call the main function.
#
main() # Displays everywhere "OK" : OK.