def reverseWord(s):
    #your code here
    str = list(s)
    strrev = ""
    for chara in reversed(str):
        strrev+=chara
    
    return strrev
