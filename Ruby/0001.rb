# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    # Create a hash to store the number and its index
    num_to_index = {}
    
    # Iterate through the list
    nums.each_with_index do |num, i|
      # Calculate the complement that would sum to the target
      complement = target - num
      
      # If the complement is found in the hash, return the indices
      if num_to_index.has_key?(complement)
        return [num_to_index[complement], i]
      end
      
      # Otherwise, add the number and its index to the hash
      num_to_index[num] = i
    end
    
    # In case no solution is found, return an empty array (though the problem assumes one solution exists)
    []
end