
def subSequence(word):    
    if word == '':
        return [""]
    
    rest = subSequence(word[1:])
    
    ans = [word[0]+i for i in rest]
    
    ans.extend(rest)

    return ans

print(subSequence('abc'))