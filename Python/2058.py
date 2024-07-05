# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # If the list has fewer than 3 nodes, return [-1, -1] since no critical points can exist
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        # List to store the indices of critical points
        critical_points = []
        # Index starts at 1 because we start checking from the second node
        idx = 1
        # Initialize pointers for previous, current, and next nodes
        prev, curr, next = head, head.next, head.next.next

        # Traverse the linked list
        while next:
            # Check if current node is a critical point (local min or max)
            if (curr.val > prev.val and curr.val > next.val) or (curr.val < prev.val and curr.val < next.val):
                # If it's a critical point, append its index to the list
                critical_points.append(idx)
            # Move the pointers one step forward
            prev, curr, next = curr, next, next.next
            # Increment the index
            idx += 1

        # If fewer than 2 critical points are found, return [-1, -1]
        if len(critical_points) < 2:
            return [-1, -1]

        # Initialize min_distance with infinity
        min_distance = float('inf')
        # Calculate the minimum distance between any two consecutive critical points
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])

        # Calculate the maximum distance between the first and last critical points
        max_distance = critical_points[-1] - critical_points[0]

        # Return the minimum and maximum distances
        return [min_distance, max_distance]
