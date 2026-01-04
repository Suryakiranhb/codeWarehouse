#944. Delete Columns to Make Sorted
strs = ["sksd","ksss","ttdf"]
strs = ["cba","daf","ghi"]
strs = ["rrjk","furt","guzm"]
interized = ord(strs[0][0])
print(type(interized))
print(interized)

#y = enumerate(strs)
#print(y)
def minDeletionSize(strs):
    word_len = len(strs[0])
    deletions = 0
    #print(word_len)
    for i in range(0,word_len):
        prev_word = -1
        for j in range(0,len(strs)):
            #print(strs[j][i])
            if ord(strs[j][i]) >= prev_word:
                prev_word = ord(strs[j][i])
                continue
            else:
                deletions+=1
                break
        #print("vertical slice complete for i level",i)
    return deletions

ans = minDeletionSize(strs)
print("The deletions would be : ",ans)