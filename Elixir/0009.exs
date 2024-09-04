defmodule Solution do
  @spec is_palindrome(x :: integer) :: boolean
  def is_palindrome(x) do
    # Handle negative numbers and numbers ending in zero (except zero itself)
    if x < 0 or (rem(x, 10) == 0 and x != 0) do
      false
    else
      reversed = reverse_number(x)
      x == reversed
    end
  end

  # Helper function to reverse the number
  defp reverse_number(x) do
    reverse_number(x, 0)
  end

  defp reverse_number(0, reversed), do: reversed

  defp reverse_number(x, reversed) do
    digit = rem(x, 10)
    reverse_number(div(x, 10), reversed * 10 + digit)
  end
end
