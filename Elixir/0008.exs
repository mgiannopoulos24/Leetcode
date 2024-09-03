defmodule Solution do
  @spec my_atoi(s :: String.t()) :: integer
  def my_atoi(s) do
    s
    |> String.trim_leading()
    |> parse_sign()
    |> parse_digits()
    |> clamp_to_32bit()
  end

  defp parse_sign(s) do
    case s do
      "-" <> rest -> {:negative, rest}
      "+" <> rest -> {:positive, rest}
      _ -> {:positive, s}
    end
  end

  defp parse_digits({sign, s}) do
    digits = s |> String.graphemes() |> Enum.take_while(&String.match?(&1, ~r/^\d$/))
    number = if digits == [], do: 0, else: String.to_integer(Enum.join(digits))
    {sign, number}
  end

  defp clamp_to_32bit({sign, number}) do
    max_int = 2_147_483_647
    min_int = -2_147_483_648

    clamped_number =
      case sign do
        :negative -> max(min_int, -number)
        :positive -> min(max_int, number)
      end

    clamped_number
  end
end
