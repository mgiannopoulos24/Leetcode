defmodule Solution do
  @spec two_sum(nums :: [integer], target :: integer) :: [integer]
  def two_sum(nums, target) do
    nums
    |> Enum.with_index()
    |> Enum.reduce_while(%{}, fn {num, index}, num_to_index ->
      complement = target - num

      case Map.get(num_to_index, complement) do
        nil ->
          # Add the current number and its index to the map
          {:cont, Map.put(num_to_index, num, index)}

        complement_index ->
          # Return the indices of the complement and the current number
          {:halt, [complement_index, index]}
      end
    end)
  end
end
