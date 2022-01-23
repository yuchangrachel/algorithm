'''
    TOPIC:math digit number
    STEP:
    1.check constraint, 10^9 is max, so can do start digit [1,10). and also need temp total num and nexter.
    2.two nested loops, outer for starting digit, inner for checking total num if in [low,high]
    '''
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for digit in range(1, 10):
            num = nexter = digit
            
            while num <= high and nexter < 10:
                if num >= low:
                    res.append(num)
                nexter += 1
                num = num * 10 + nexter
        return sorted(res)
        
    
print(sequentialDigits(100, 300))