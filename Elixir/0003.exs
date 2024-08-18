defmodule Solution do
  @spec length_of_longest_substring(s :: String.t()) :: integer
  def length_of_longest_substring(s) do
    {max_length, _, _} = 
      s
      |> String.graphemes()
      |> Enum.with_index()
      |> Enum.reduce({0, 0, %{}}, fn {char, right}, {max_length, left, char_map} ->
        left = 
          if Map.has_key?(char_map, char) && char_map[char] >= left do
            char_map[char] + 1
          else
            left
          end

        char_map = Map.put(char_map, char, right)

        max_length = max(max_length, right - left + 1)

        {max_length, left, char_map}
      end)

    max_length
  end
end
