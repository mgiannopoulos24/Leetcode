from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Dictionary to hold lists of people by their group sizes
        size_to_people = defaultdict(list)
        result = []
        
        # Iterate over each person and their required group size
        for person, group_size in enumerate(groupSizes):
            size_to_people[group_size].append(person)
            
            # If the list reaches the desired group size, we form a group
            if len(size_to_people[group_size]) == group_size:
                result.append(size_to_people[group_size])
                size_to_people[group_size] = []  # Reset the list for that group size
        
        return result
