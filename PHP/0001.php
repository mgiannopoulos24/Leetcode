class Solution {

/**
 * @param Integer[] $nums
 * @param Integer $target
 * @return Integer[]
 */
    function twoSum($nums, $target) {
        // Create an associative array to store the number and its index
        $numToIndex = [];
        
        // Iterate through the array
        foreach ($nums as $i => $num) {
            // Calculate the complement that would sum to the target
            $complement = $target - $num;
            
            // If the complement is found in the array, return the indices
            if (array_key_exists($complement, $numToIndex)) {
                return [$numToIndex[$complement], $i];
            }
            
            // Otherwise, add the number and its index to the array
            $numToIndex[$num] = $i;
        }
        
        // Return an empty array if no solution is found (though problem guarantees one)
        return [];
    }
}