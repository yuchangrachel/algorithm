'''
    LOGIC:
    1.change chars array in-place, so need cur index track original array, return res index
    2.How to do pointer when count > 1, need replace original slot
'''

def compress(self, chars):
        if not chars or len(chars) == 0: return 0
        self.resIndex = 1 # after in-place, return resIndex
        section_count = 1 # cur section's count
        prev_char = chars[0] 
        
        
        def appendCount(chars, count): # void
            if count > 1:
                if count > 9:
                    for c in str(count):
                        chars[self.resIndex] = c
                        self.resIndex += 1
                else:
                    chars[self.resIndex] = str(count)
                    self.resIndex += 1
                    
        
        for i in range(1, len(chars)):
            if chars[i] == prev_char:
                section_count += 1
            else:
                # check previous section
                appendCount(chars, section_count)
                
                # new section
                chars[self.resIndex] = chars[i] # add cur character
                self.resIndex += 1 # for use it later
                section_count = 1 # reset
                prev_char = chars[i]
                
        # last section
        appendCount(chars, section_count)            
        return self.resIndex #now is len-1+1
    