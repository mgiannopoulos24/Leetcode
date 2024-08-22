defmodule Solution do
  @spec longest_palindrome(s :: String.t) :: String.t
  def longest_palindrome(s) do
    len = String.length(s)
    map =
      String.to_charlist(s)
      |> Enum.with_index(fn ch, i -> {i * 2 + 2, ch} end)
      |> Map.new()
      |> Map.merge(%{0 => ?^, len * 2 + 2 => ?$})

    (2..len * 2)
    |> Enum.reduce({1, 0, %{}, 1, 1}, fn i, {ans, width, dp, l, r} ->
      val =
        Map.get(dp, r + l - i, 0)
        |> min(r - i)
        |> check_palin(i, map)
        
      {ans, width} = if val > width, do: {i, val}, else: {ans, width}
      {l, r} = if i + val > r, do: {i - val, i + val}, else: {l, r}
      {ans, width, Map.put(dp, i, val), l, r}
    end)
    |> then(fn {ans, width, _, _, _} ->
      ans - width + 1..ans + width - 1
    end)
    |> Enum.map(&Map.get(map, &1, ?#))
    |> Enum.filter(fn ch -> ch != ?# end)
    |> to_string()
  end

  defp check_palin(val, i, map) do
    if Map.get(map, i - val, ?#) == Map.get(map, i + val, ?#) do
      check_palin(val + 1, i, map)
    else
      val
    end
  end
end