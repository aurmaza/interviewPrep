def canFinish(numCourses, prerequisites):
    preMap = { i:[] for i in range(numCourses)}
    for course, pre in prerequisites:
        preMap[course].append(pre)
    visited = set()
    def dfs(course):
        if course in visited:
            return False
        if preMap[course] == []:
            return True
        visited.add(course)
        for prereq in preMap[course]:
            if not dfs(prereq): return False
        visited.remove(course)
        preMap[course] = []
        return True
    for course in range(numCourses):
        if not dfs(course):return False
    return True

if __name__ == "__main__":
    test1=[[1,0]]
    test2=[[1,0],[0,1]]
    test3=[[1,0],[2,1],[2,3],[3,2]]
    test4=[[1,0],[2,1],[2,3],[3,4]]
    print(canFinish(2,test1))
    print(canFinish(2,test2))
    print(canFinish(4,test3))
    print(canFinish(5, test4))