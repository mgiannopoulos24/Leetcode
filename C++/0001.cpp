#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(const std::vector<int>& nums, int target) {
        // Create an unordered map to store the number and its index
        std::unordered_map<int, int> num_to_index;
        
        // Iterate through the list
        for (int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            int complement = target - num;
            
            // If the complement is found in the map, return the indices
            if (num_to_index.find(complement) != num_to_index.end()) {
                return {num_to_index[complement], i};
            }
            
            // Otherwise, add the number and its index to the map
            num_to_index[num] = i;
        }
        
        // Return an empty vector if no solution is found (though the problem assumes one exists)
        return {};
    }
};
