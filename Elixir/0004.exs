defmodule Solution do
  @spec find_median_sorted_arrays(nums1 :: [integer], nums2 :: [integer]) :: float
  def find_median_sorted_arrays(nums1, nums2) do
    # Ensure nums1 is the smaller array to make the binary search more efficient
    if length(nums1) > length(nums2) do
      find_median_sorted_arrays(nums2, nums1)
    else
      binary_search(nums1, nums2, 0, length(nums1))
    end
  end

  defp binary_search(nums1, nums2, low, high) do
    m = length(nums1)
    n = length(nums2)

    if low <= high do
      i = div(low + high, 2)
      j = div(m + n + 1, 2) - i

      max_left_1 = if i == 0, do: -1.0e308, else: Enum.at(nums1, i - 1)
      min_right_1 = if i == m, do: 1.0e308, else: Enum.at(nums1, i)
      
      max_left_2 = if j == 0, do: -1.0e308, else: Enum.at(nums2, j - 1)
      min_right_2 = if j == n, do: 1.0e308, else: Enum.at(nums2, j)

      if max_left_1 <= min_right_2 and max_left_2 <= min_right_1 do
        # Found the correct partition
        if rem(m + n, 2) == 0 do
          (max(max_left_1, max_left_2) + min(min_right_1, min_right_2)) / 2
        else
          max(max_left_1, max_left_2)
        end
      else
        if max_left_1 > min_right_2 do
          binary_search(nums1, nums2, low, i - 1)
        else
          binary_search(nums1, nums2, i + 1, high)
        end
      end
    end
  end
end
