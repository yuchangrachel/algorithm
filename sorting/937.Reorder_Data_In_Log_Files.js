var reorderLogFiles = function (logs) {
  if (logs == null || logs.length == 0) return [];

  //creat two array for one digit group and another letter group
  const digits = [];
  const letters = [];
  for (let log of logs) {
    if (!isNaN(log[log.length - 1])) {
      //it is digit log
      digits.push(log);
    } else {
      letters.push(log);
    }
  }

  // sort letters perspectively
  letters.sort((a, b) => {
    let strA = a.substr(a.indexOf(" ") + 1);
    let strB = b.substr(b.indexOf(" ") + 1);

    if (strA === strB) return a.localeCompare(b);
    else return strA.localeCompare(strB);
  });

  // push them together and return
  return [...letters, ...digits];
};

/*
def reorderLogFiles(self, logs: List[str]) -> List[str]:
        '''
        two part: letterlog + digitlog
        letterlog sort letterlog[1:], then sort [0]
        digitlog order is same
        '''
        # separate two groups
        letters = []
        digits = []
        
        for log in logs:
            if log[-1].isalpha():
                letters.append(log)
            else:
                digits.append(log)
        
        #sort letters
        def helper(a,b):
            a2 = a.split(" ")[1:]
            b2 = b.split(" ")[1:]

            if a2 < b2: return -1
            elif a2 > b2: return 1
            else: return 0
  
            
        letters.sort() #sort identifier
        letters.sort(key=cmp_to_key(helper))
            
        return letters + digits
    
*/
