defmodule Solution do
  @spec reverse(x :: integer) :: integer
  def reverse(x) do
    # Define the 32-bit signed integer range
    min_int = -2_147_483_648
    max_int = 2_147_483_647

    # Check if the input is negative
    negative = x < 0

    # Work with the absolute value of x
    x_abs = abs(x)

    # Reverse the digits of the absolute value
    reversed_str = Integer.to_string(x_abs)
    |> String.reverse()
    |> String.to_integer()

    # Apply the original sign to the reversed integer
    reversed_int = if negative, do: -reversed_str, else: reversed_str

    # Check for overflow and return the result
    if reversed_int < min_int or reversed_int > max_int do
      0
    else
      reversed_int
    end
  end
end
