# Plan
# 1. Build a graph mapping to each course to its prerequisites
# 2. Maintain a visiting set for cycle detection
# 3. Maintain a completed set to avoid processing the same course twice
# 4. Use DFS to process all prerequisites before appending the current course
# 5. Return an empty list if any cycle is detected

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {course: [] for course in range(numCourses)}
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        visiting = set() # Courses in the current DFS path
        completed = set() # Courses already fully processed
        order = [] # Valid course order

        def dfs(course):
            if course in visiting:
                return False # Cycle detected
            if course in completed:
                return True # Already processed successfully
            visiting.add(course)

            # Finish prerequisites before the current course
            for prerequisite in graph[course]:
                if not dfs(prerequisite):
                    return False
            visiting.remove(course)
            completed.add(course)
            order.append(course) # Add only after prerequisites
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return order