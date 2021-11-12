from collections import defaultdict
def findDuplicate(paths):
        '''
        TOPIC: String problem +hash table
        THINK: Divide groups with different contents, if this is same content, put into same group
        HOW:
        {content: [path1, path2]}
        '''
        if not paths or len(paths) == 0: return []
        dic = defaultdict(list)
        
        for path in paths:
            part = path.split(" ")
            directory = part[0]
            
            for i in range(1, len(part)):
                contents = part[i].split(".")
                no = contents[0]
                content = contents[1]
                road = ""
                road += directory+"/"+ no + ".txt"
                if content not in dic:
                    dic[content] = [road]                    
                else:
                    dic[content].append(road)
        
        res = []
        for v in dic.values():
            if len(v) > 1:
                res.append(v)      
        return res
                    
print(findDuplicate(["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]))