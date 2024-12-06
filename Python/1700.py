class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Count the number of students preferring each type of sandwich
        count_0 = students.count(0)  # Students preferring circular sandwiches (0)
        count_1 = students.count(1)  # Students preferring square sandwiches (1)
        
        # Go through each sandwich in the stack
        for sandwich in sandwiches:
            if sandwich == 0:
                if count_0 > 0:
                    count_0 -= 1  # A student takes the circular sandwich
                else:
                    return count_1  # No more students who want circular sandwiches
            else:
                if count_1 > 0:
                    count_1 -= 1  # A student takes the square sandwich
                else:
                    return count_0  # No more students who want square sandwiches
        
        # If all students are able to eat
        return 0
