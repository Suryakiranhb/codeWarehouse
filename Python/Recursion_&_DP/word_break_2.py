# WORD BREAK 2, wherein theres gonna be a single string,using which we have to insert spaces so that it becomes a word given in a predetermined list

def wordBreak(s, wordDict):
    word_set = set(wordDict)
    memo = {}

    def dfs(start):
        if start == len(s):
            return [""]

        if start in memo:
            return memo[start]
        
        res = []
        for end in range(start+1, len(s)+1):
            prefix = s[start:end]
            if prefix in word_set:
                for tail in dfs(end):
                    res.append(prefix + (" " + tail if tail else ""))
        memo[start] = res
        return res
    
    return dfs(0)

s = "pineapplepenapple"
wordDict=["apple","pen","applepen","pine","pineapple"]
ans = wordBreak(s,wordDict)
print("The dict s can be broken down into: ",ans)














s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
wordBreak(s,wordDict)

## Dry run:
"""
So, initially the wordbreak function is called with the string and the list of the words. 
We initialize word_set as a set of wordDict in order to eliminate any duplicates. 
Then, we initialize a memo set. Then the return statement is reached, which runs the dfs function with start = 0.
Start wont be len(s), and start wont be in memo. Res list is initialized, then, it iterates through 0+1, till length of s +1,
this is because we need to catch if it reaches len+1 as it means we have run out of words and still have nothing in memo, thereby to return "", we iterate till len(s)+1.
Now, prefix is s[1:1]. This will mean the word is 'c'. this 'c' wont be in word_set. so for loop will go to next iteration. 
this will make prefix be ca and then cat, and when it reaches cat, this is present in word_dict. 
So now, the inner for loop will start. Until here I am clear. And I hope I am correct until now. 
After this, is where I get into confusion, as are we recursing in the for loop itself? thats crazy! So that would mean we are calling dfs(3).
So now, it will fail both if conditions and come to the for loop again, this time, starting from 4. Like this, we are calling recursion each time we get a word which is present in wordDict.
Then we are appending the words when we come back from recursion, and then, weare saving all those in memo[start].

Am I correct?

"""