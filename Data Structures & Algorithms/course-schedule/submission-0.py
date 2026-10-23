
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course: [] for course in range(numCourses)}
        # Build graph: course -> its prerequisites
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        visiting = set() # Courses currently in the DFS path
        def dfs(course):
            if course in visiting:
                return False # Cycle detected
            if not graph[course]:
                return True # No remaining prerequisites
            visiting.add(course) # Enter the current DFS path
            for prerequisite in graph[course]:
                if not dfs(prerequisite):
                    return False # A dependency contains a cycle
            visiting.remove(course) # Finished exploring this course
            graph[course] = [] # Mark as fully processed
            return True
        # Every course must be free of cycles
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True