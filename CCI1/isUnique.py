'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures? 
'''
def isUnique(s):
    letters = set()#create an empty set
    chars = list(s)
    for c in chars:
        if c in letters:
            return False
        letters.add(c)
    return True
            
    






if __name__ == "__main__":
    print(isUnique("abc"))
    print(isUnique("aabb"))
    
    