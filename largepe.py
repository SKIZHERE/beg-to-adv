strs = ["flower","flow","flight"]
strs.sort()
print(strs)
n = 0
for i in range(len(strs[0])): 
    if strs[0][n] == strs[-1][n]:
        n+=1
        continue
    else:
        print(strs[0][:n])
        break
