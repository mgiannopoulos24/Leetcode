def find_median_sorted_arrays(nums1, nums2)
    # Ensure nums1 is the smaller array
    if nums1.length > nums2.length
      nums1, nums2 = nums2, nums1
    end
  
    m, n = nums1.length, nums2.length
    imin, imax, half_len = 0, m, (m + n + 1) / 2
    
    while imin <= imax
      i = (imin + imax) / 2
      j = half_len - i
      
      if i < m && nums2[j - 1] > nums1[i]
        imin = i + 1
      elsif i > 0 && nums1[i - 1] > nums2[j]
        imax = i - 1
      else
        max_of_left = if i == 0
                        nums2[j - 1]
                      elsif j == 0
                        nums1[i - 1]
                      else
                        [nums1[i - 1], nums2[j - 1]].max
                      end
  
        if (m + n) % 2 == 1
          return max_of_left.to_f
        end
  
        min_of_right = if i == m
                         nums2[j]
                       elsif j == n
                         nums1[i]
                       else
                         [nums1[i], nums2[j]].min
                       end
  
        return (max_of_left + min_of_right) / 2.0
      end
    end
  end
  