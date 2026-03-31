class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites: 
            prereqs[course].append(pre)

        # visit set = store all courses in CURRENT DFS path 
        visited = set()
        def dfs(course): 
            if course in visited: 
                return False 
            if prereqs[course] == []: 
                return True 

            visited.add(course)
            for item in prereqs[course]: 
                if not dfs(item): 
                    return False 
            
            visited.remove(course)
            prereqs[course] = []
            return True

        for course in range(numCourses): 
            if not dfs(course): 
                return False 
        
        return True 