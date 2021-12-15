'''
    TOPIC:string+count pointer, modify result in-place, need INDEX+POINTER
    STEP:
    1.create helper appendcountNum(->str)for prev section, triggered when != flagChar
    '''
    def compress(self, chars: List[str]) -> int:
        if not chars or len(chars) == 0: return 0
        # self.cur = result len
        self.cur = 1
        flag = chars[0]
        sectionCount = 1
        def appendCount(count):
            #if count <= 1 return single char
            if count > 1:
                for c in str(count):#Ndigits
                    chars[self.cur] = c #replaced
                    self.cur += 1
                              
        for i in range(1, len(chars)):
            if chars[i] == flag:
                sectionCount += 1
            else:
                #count prev section,now trigger appendCount helper method
                appendCount(sectionCount)
                #start new section
                flag = chars[i]
                chars[self.cur] = flag #replaced
                self.cur += 1 #count newchar
                sectionCount = 1
        
        #last section
        appendCount(sectionCount)
        return self.cur
