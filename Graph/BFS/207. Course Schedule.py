'''
    TOPIC:all actions have prerequisite, GRAPH make relations clean
    STEp:How to handle graph.1way:2D 2way:neighbor list
    1.[totake: preq], create hashmap store {preq:[list of totake]}
    2.create indegree array store number of preqre for course
    3.create queue, if indegree[i]==0, push, mean no preq
    4.if check indegree array, if some !=0, mean still preq didnt finish, so return False
'''
from collections import defaultdict
from collections import deque
def canFinish(numCourses,prerequisites):
        indegree = [0] * numCourses
        for pre in prerequisites:
            indegree[pre[0]] += 1 # add preq num
            
        graph = defaultdict(list)
        for pre in prerequisites:
            if pre[1] not in graph:
                graph[pre[1]] = []
            graph[pre[1]].append(pre[0])
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i) #!!!
                
        while len(q) > 0:
            cur = q.popleft()
            totakes = graph[cur] # later courses list
            for course in totakes:
                indegree[course] -= 1
                if indegree[course] == 0: # no preq anymore
                    q.append(course)
        
        print(indegree)
        for i in range(numCourses):
            if indegree[i] != 0:
                return False
        
        return True

print(canFinish(2,[[0,1]]))


'''
210. Course Schedule II

    LOGIC:similar to Course Schedule I
    STEP:
    1.when indegree == 0 into final res
'''
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        # indegree count number of preq for this cur course
        # dic store {preq:list of latter course}
        dic = collections.defaultdict(list)
        for pre in prerequisites:
            indegree[pre[0]]+=1
            
            if pre[1] not in dic:
                dic[pre[1]] = []
            dic[pre[1]].append(pre[0])

        #create q, push no preq ones, and level by level
        q = collections.deque()
        res = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                res.append(i)

        while len(q) > 0:
            cur = q.popleft()
            latterList = dic[cur]

            for i in range(len(latterList)):
               
                indegree[latterList[i]] -= 1

                if indegree[latterList[i]] == 0:
                    q.append(latterList[i])
                    res.append(latterList[i])
        
        #check if finish all courses
        for i in range(numCourses):
            if indegree[i] != 0:
                return []
        return res
        