class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pres = {course: list() for course in range(numCourses)}
        posts = {course: list() for course in range(numCourses)}
        zeroes = {i for i in range(numCourses)}

        for [pre, post] in prerequisites:
            if post in zeroes:
                zeroes.remove(post)
            pres[post].append(pre)
            posts[pre].append(post)
        # print(pres)
        
        visited = zeroes.copy()
        learned = zeroes.copy()
        # print(zeroes, learned)
        while len(zeroes) > 0:
            for pre in zeroes:
                visited.add(pre)
                postreqs = posts[pre]
                for post in postreqs:
                    prereqs = pres[post]
                    if len(prereqs) == 1:
                        learned.add(post)
                    pres[post].remove(pre)

            # print(f"Learned {learned} visited {visited}")
            zeroes = learned - visited
            # print(zeroes)

        if len(learned) ==  numCourses:
            return True
        else:
            return False