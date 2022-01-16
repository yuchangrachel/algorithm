# 1.Divide a String into Groups of Size K
def divideString(s, k, fill):
        res = []
        for i in range(0,len(s), k):
            print(i)
            if i + k <= len(s):
                res.append(s[i:i+k])
                print(res)
            else:
                # need fill
                laststr = s[i:]
                while len(laststr) < k:
                    laststr += fill
                res.append(laststr)
        
        return res

# print(divideString("abcdefghi",3,"x"))

'''
2.
Minimum Moves to Reach Target Score
User Accepted:5309
User Tried:6450
Total Accepted:5392
Total Submissions:11618
Difficulty:Medium
You are playing a game with integers. You start with the integer 1 and you want to reach the integer target.

In one move, you can either:

Increment the current integer by one (i.e., x = x + 1).
Double the current integer (i.e., x = 2 * x).
You can use the increment operation any number of times, however, you can only use the double operation at most maxDoubles times.

Given the two integers target and maxDoubles, return the minimum number of moves needed to reach target starting with 1.
Example 1:

Input: target = 5, maxDoubles = 0
Output: 4
Explanation: Keep incrementing by 1 until you reach target.
Example 2:

Input: target = 19, maxDoubles = 2
Output: 7
Explanation: Initially, x = 1
Increment 3 times so x = 4
Double once so x = 8
Increment once so x = 9
Double again so x = 18
Increment once so x = 19
Example 3:

Input: target = 10, maxDoubles = 4
Output: 4
Explanation: Initially, x = 1
Increment once so x = 2
Double once so x = 4
Increment once so x = 5
Double again so x = 10
'''
def minMoves(target, maxDoubles):
        if maxDoubles == 0: 
            return target - 1
        
        step = 0
        n = target
        while n >= 2 and maxDoubles > 0:
            digit = n//2
            step += n - digit * 2 +1
            n //= 2
            maxDoubles -= 1
        
        step += n- 1
        
        return step
# print(minMoves(19,2))
        
'''
3.
Solving Questions With Brainpower
User Accepted:3157
User Tried:4892
Total Accepted:3227
Total Submissions:9494
Difficulty:Medium
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.

 

Example 1:

Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
Example 2:

Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: 7
Explanation: The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
'''
'''
    TOPIC:DP question
    two choices:first choice:pick now:current earn + dp[i + questions[i][1] + 1]; or pass next:dp[i+1]
    dp[i] mean max points. since need to know latter of dp, so can traverse backword
    dp set 1d default 0 size +1
    '''
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp =[0] * (len(questions) + 1)
        for i in range(len(questions)-1, -1, -1):
            earn = questions[i][0]
            nexter = questions[i][1]
            dp[i] = max(earn + dp[min(len(questions), i + nexter + 1)], dp[i+1]) #avoid index overflow set min, dp size+1 since dp[i+1]
            
        
        return dp[0]
        

print(mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]])) #157