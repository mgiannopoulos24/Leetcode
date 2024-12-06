from collections import defaultdict

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count_triplets(arr1, arr2):
            count = 0
            for i in range(len(arr1)):
                target = arr1[i] * arr1[i]
                product_map = defaultdict(int)
                for j in range(len(arr2)):
                    if target % arr2[j] == 0:
                        complement = target // arr2[j]
                        if complement in product_map:
                            count += product_map[complement]
                    product_map[arr2[j]] += 1
            return count
        
        # Count Type 1 triplets (nums1[i]^2 == nums2[j] * nums2[k])
        count_type_1 = count_triplets(nums1, nums2)
        
        # Count Type 2 triplets (nums2[i]^2 == nums1[j] * nums1[k])
        count_type_2 = count_triplets(nums2, nums1)
        
        return count_type_1 + count_type_2
