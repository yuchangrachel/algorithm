'''
    LOGIC:
    1.split many pars as possible, each letter only appear at most one part.
    2.hashmap store{char:rightmost}
    3.three pointer left and right tracking string, compare right and rightmost, update right, get longest valid substring
    4.left pointer start new part, i is cur pos, leftmost is farthest.
    
'''
def partitionLabels(s):
        if not s or len(s) == 0: return []
        
        dic = {}
        res = []
        for i, char in enumerate(s):
            dic[char] = i #will update to rightmost index
        print(dic)

        left = rightmost = 0
        for i, letter in enumerate(s):
            rightmost = max(rightmost, dic[letter])
            if i == rightmost:
                print(i, " ", left)
                res.append(rightmost - left + 1)
                left = 1+i
        return res
print(partitionLabels(("ababcbacadefegdehijhklij")))
'''
0-8 9-15
ababcbaca defegde hijhklij
'''