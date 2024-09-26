defmodule Solution do
  @spec roman_to_int(s :: String.t()) :: integer
  def roman_to_int(s) do
    roman_map = %{
      ?I => 1,
      ?V => 5,
      ?X => 10,
      ?L => 50,
      ?C => 100,
      ?D => 500,
      ?M => 1000
    }

    s
    |> String.to_charlist()
    |> Enum.reverse()
    |> Enum.reduce({0, 0}, fn char, {total, prev_value} ->
      current_value = Map.get(roman_map, char)

      if current_value < prev_value do
        {total - current_value, current_value}
      else
        {total + current_value, current_value}
      end
    end)
    |> elem(0)
  end
end
