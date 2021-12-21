'''
276. Paint Fence
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.
Note: n and k are non-negative integers.
Example:
Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3      
 -----      -----  -----  -----       
   1         c1     c1     c2
   2         c1     c2     c1
   3         c1     c2     c2
   4         c2     c1     c1  
   5         c2     c1     c2
   6         c2     c2     c1
'''
'''
TOPIC: no more than two adjacent fence have same color(similar to Robber house) -> DP statistic
STEP:
 k-1 k
X,Y=>Z

same[k]: # of painting method that meet nums[k-1]=nums[k](k is same as k-1, the k-1 must diff from k-2)
diff[k]: # of painting method that meet nums[k-1]!=nums[k](k is diff as k-1, so k-1 can same/diff k-2)
same[k]=diff[k-1]
diff[k]=same[k-1]*(k-1) + diff[k-1]*(k-1)
return same+diff(because all possiblity)
eg.
RGB three colors
same:same=k(1st k, 2nd k)
R R 
G G 
B B 
diff:diff=k*(k-1) (1st k, 2nd k-1)
pick R, so left GB.(2ways:R,G,B or R,B,G)
pick G, so left RB.(2ways)
pick B, so left RG.(2ways)
so mean combination possiblity(statistic): color#*(color#-1)=3*2=6
'''
def numWays(n,k):
  if n == 0: return 0
  if n == 1: return k
  #n=2
  same = k
  diff = k*(k-1)
  for i in range(3, n+1):
    same_temp = same
    diff_temp = diff
    diff = same_temp*(k-1) + diff_temp*(k-1)
    same = diff_temp
  return same+diff

print(numWays(3,2))