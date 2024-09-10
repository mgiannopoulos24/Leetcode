defmodule Solution do
  @spec int_to_roman(integer) :: String.t()
  def int_to_roman(num) do
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    int_to_roman(num, values, symbols, "")
  end

  defp int_to_roman(0, _values, _symbols, result), do: result

  defp int_to_roman(num, [value | rest_values], [symbol | rest_symbols], result) do
    if num >= value do
      int_to_roman(num - value, [value | rest_values], [symbol | rest_symbols], result <> symbol)
    else
      int_to_roman(num, rest_values, rest_symbols, result)
    end
  end
end
