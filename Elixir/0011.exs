defmodule Solution do
  @spec max_area(height :: [integer]) :: integer
  def max_area(height) do
    tuple_height = List.to_tuple(height)
    max_area(tuple_height, 0, length(height) - 1, 0)
  end

  defp max_area(_, left, right, max_area) when left >= right do
    max_area
  end
  
  defp max_area(tuple_height, left, right, max_area) do
    left_height = elem(tuple_height, left)
    right_height = elem(tuple_height, right)
    width = right - left
    current_area = min(left_height, right_height) * width
    new_max_area = max(max_area, current_area)
    
    if left_height < right_height do
      max_area(tuple_height, left + 1, right, new_max_area)
    else
      max_area(tuple_height, left, right - 1, new_max_area)
    end
  end
end
