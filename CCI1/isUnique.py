'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures? 
'''


from wsgiref.validate import validator


def isUnique(s):
    if len(s) > 128:
        return False  # String is assumed to be ASCII

    letters = set()  # create an empty set
    chars = list(s)
    for c in chars:
        if c in letters:
            return False
        letters.add(c)
    return True


def isUniqueAlgorithm(s):
    if len(s) > 128:
        return False
    asciiVals = [False] * 128
    for c in s:
        temp = ord(c)
        if asciiVals[temp]:
            return False
        asciiVals[temp] = True
    return True


'''
Review of Binary Operators
Compliment Operator "~"
~12 result? -13
~-13 --> 12
~300
->-301
Ampersand Operator "&"
12&13?
00001100
&
00001101
--
00001100 = 12
Or Operation "|"
00001100
|
000001101
---
00001101 = 13
XOR Operator "^"
0 0 -> 0
0 1 -> 1
1 0 -> 1
1 1 -> 0
25 ^ 30
0001 1001
^
0001 1110
--
00000111 = 7
Left Shift "<<"
10 << 2

00001010
00101000 = 40
Right Shift ">>"
10 >> 2
00001010
00000010 = 2

'''


def isUniqueBitVector(s):
    if len(s) > 128:
        return False
    validator = 0
    for c in s:
        value = ord(c)
        print(validator)
        print(1<<value)
        if(validator & (1<<value)) > 0:
            return False
        validator |= 1 << value
    return True

if __name__ == "__main__":
    print(isUnique("abc"))
    print(isUnique("!helo!"))
    print(isUniqueAlgorithm("abc"))
    print(isUniqueAlgorithm("!helo!"))
    print(isUniqueBitVector("!helo!"))