#151
# T:O(n) S(n)
def reverseWords(s):
        if s is None or len(s) == 0: return s
        arr = s.split(" ")[::-1]
        res = []
        for word in arr:
            if word == '':
                continue
            else:
                res.append(word)
        return " ".join(res)
# print(reverseWords(("  hello world ")))


# 186
'''
Given an input string, reverse the string word by word.
Example:
Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 
A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.The words are always separated by a single space.
Follow up: Could you do itin-placewithout allocating extra space?
'''
def reverseWords2(charList):
    i = 0
    helper(charList,0, len(charList) - 1)
    for j in range(len(charList)+1):
        if j == len(charList) or charList[j] == " ":
            helper(charList, i, j-1)
            i = j+1
    return charList

def helper(sublist, start, end):
    while start < end: #dont need = for more efficiency
        temp = sublist[start]
        sublist[start] = sublist[end]
        sublist[end] = temp
        start += 1
        end -= 1


print(reverseWords2(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))
