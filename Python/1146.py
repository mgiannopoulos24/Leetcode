from collections import defaultdict
import bisect

class SnapshotArray:

    def __init__(self, length: int):
        # Initialize an array of dictionaries to store the snapshots of each index
        # Each index will store a list of (snap_id, value) pairs
        self.snapshots = defaultdict(list)
        self.snap_id = 0  # Initially, snap_id is 0 for the first snapshot
        
        # Initialize each index of the array with a default value of 0
        for i in range(length):
            self.snapshots[i].append((0, 0))

    def set(self, index: int, val: int) -> None:
        # Append the value to the snapshot list of the given index with the current snap_id
        # Check if the last added snap_id is the same, update value in place if it is
        if self.snapshots[index][-1][0] == self.snap_id:
            self.snapshots[index][-1] = (self.snap_id, val)
        else:
            self.snapshots[index].append((self.snap_id, val))

    def snap(self) -> int:
        # Increment the snap_id and return the previous one
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Use binary search to find the latest snapshot <= snap_id for the given index
        snapshot_list = self.snapshots[index]
        i = bisect.bisect_right(snapshot_list, (snap_id, float('inf'))) - 1
        return snapshot_list[i][1]




# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)