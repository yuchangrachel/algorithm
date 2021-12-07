#93. Restore IP Addresses
'''
    TOPIC:ask valid IP Adress, four parts and three dots, 0<=part<=255
    STEP:
    1.Think backtracking, helper with parameters: subIp, index for searching string, dot#
    2.dfs(for(1 to 4)) because show all combination, each section may has 1,2,3number
    3.each section subtring[start:start+index] index(1~4), think out of boundary or invalid.
    4.finally, when if at third section, after that cannot have"."
'''
def restoreIpAddresses(self, s: str) -> List[str]:
        # corner case .already took up three indices
        if len(s)<4 or not s: return []
        
        res = []
        self.dfs(s, res, 0, "", 0)
        return res
    
def dfs(self, s, res, start, subip, section):
        # only four section
        # terminate case
        if section > 4: return
        if section == 4 and start == len(s):
            res.append(subip)
            return
        
        # loop for check all combination
        # when start new section, will has 1,2,3 number 
        for index in range(1, 4, 1):
            if start + index > len(s): break
            temp = s[start: start+index]
            #check if temp valid or not
            if (s[start] == "0" and len(temp) > 1) or (int(temp) > 255): break
            self.dfs(s, res, start+index, subip + temp + ("" if section == 3 else "."), section + 1)