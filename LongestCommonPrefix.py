class Solution:
    def longestCommonPrefix(strs) -> str:        
        out = strs[0]
        for i in range(1, len(strs)):
            count = -1
            for j in range(len(strs[i])):
                if j < len(out):
                    if out[j] == strs[i][j]:
                        count+=1
            print(count)
            print(out)
            out = out[0:count+1]
        return out
        
    
    
obj = Solution
strs = ["cir", "car"]
print(obj.longestCommonPrefix(strs))
    
