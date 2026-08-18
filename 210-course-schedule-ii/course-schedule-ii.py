from typing import List

class Queue:
    def __init__(self):  # ಎರಡು ಅಂಡರ್‌ಸ್ಕೋರ್ ಇರಬೇಕು: __init__
        self.q = []
        self.front = -1

    def push(self, x):
        if self.front == -1:
            self.front = 0  # '@' ಬದಲಿಗೆ 0 ಇರಬೇಕು
        self.q.append(x)

    def pop(self):
        if len(self.q) == 0 or self.front == -1:
            return -1
        x = self.q[self.front]
        self.front += 1
        if self.front == len(self.q):
            self.front = -1
            self.q = []
        return x

    def getFront(self):
        if len(self.q) == 0 or self.front == -1:
            return -1
        return self.q[self.front]

    def size(self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = Queue()
        ans = []
        # 'n' ವೇರಿಯಬಲ್ ಇಲ್ಲ, ಅದರ ಬದಲು 'numCourses' ಬಳಸಬೇಕು
        indegree = [0] * numCourses
        adjList = []

        for i in range(numCourses):
            adjList.append([])
        
        for a, b in prerequisites:
            indegree[a] += 1
            adjList[b].append(a)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                ans.append(i)
                q.push(i)
            
        while q.size() > 0:
            front = q.pop()
            for x in adjList[front]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    ans.append(x)
                    q.push(x)
        
        if len(ans) == numCourses:
            return ans
        else:
            return []

        