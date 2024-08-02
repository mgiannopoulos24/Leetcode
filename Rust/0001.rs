use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        // Create a hash map to store the number and its index
        let mut num_to_index = HashMap::new();
        
        // Iterate through the list with indices
        for (i, &num) in nums.iter().enumerate() {
            // Calculate the complement that would sum to the target
            let complement = target - num;
            
            // If the complement is found in the hash map, return the indices
            if let Some(&index) = num_to_index.get(&complement) {
                return vec![index as i32, i as i32];
            }
            
            // Otherwise, add the number and its index to the hash map
            num_to_index.insert(num, i);
        }
        
        // If no solution is found, return an empty vector (though the problem assumes one solution exists)
        vec![]
    }
}
