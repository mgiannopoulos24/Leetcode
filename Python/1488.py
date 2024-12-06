from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # Dictionary to track when a lake was last filled
        full_lakes = {}
        # List to store the result
        result = [-1] * len(rains)
        # Sorted list to track available dry days
        dry_days = SortedList()

        for i, lake in enumerate(rains):
            if lake > 0:
                # It's raining on lake `lake`
                if lake in full_lakes:
                    # Check if there's a dry day available to dry this lake before flooding
                    dry_day_index = dry_days.bisect_left(full_lakes[lake])
                    if dry_day_index == len(dry_days):
                        # No dry day available before this lake rains again -> flood
                        return []
                    # Use the dry day to dry the lake before it rains again
                    dry_day = dry_days.pop(dry_day_index)
                    result[dry_day] = lake
                # Mark this lake as full
                full_lakes[lake] = i
            else:
                # It's a dry day, mark it as available for drying later
                dry_days.add(i)
        
        # For the remaining dry days, we can dry any arbitrary lake (assign 1)
        for day in dry_days:
            result[day] = 1
        
        return result
