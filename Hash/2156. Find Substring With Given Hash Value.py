'''
    Intuition
Good time to learn rolling hash.
what's hash?
The definition hash(s, p, m) in the description is the hash of string s based on p.

what's rolling hash?
The hash of substring is a sliding window.
So the basis of rolling hash is sliding window.

Explanation
Calculate the rolling hash backward.
In this process, we slide a window of size k from the end to the begin.

Firstly calculate the substring hash of the last k characters,
then we add one previous backward and drop the last characters.

Why traverse from end instead of front?
Because cur is reminder by mod m,
cur = cur * p works easier.
cur = cur / p doesn'r work easily.


Complexity
Time O(n)
Space O(1)
    '''
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(c):
            return ord(c) - ord("a") + 1
        
        pk = pow(power,k, modulo)
        cur = 0
        
        for i in range(len(s)-1, -1, -1):
            cur = (cur * power + val(s[i])) % modulo
            if i + k < len(s):
                cur = (cur - val(s[i+k]) * pk) % modulo
            if cur == hashValue:
                res = i
        return s[res:res+k]
        