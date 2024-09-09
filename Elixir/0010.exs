defmodule Solution do
  @spec is_match(s :: String.t(), p :: String.t()) :: boolean
  def is_match(s, p) do
    memo = :ets.new(:memo, [:set, :public, :named_table])
    result = is_match_helper(s, p, 0, 0, String.length(s), String.length(p), memo)
    :ets.delete(:memo)
    result
  end

  defp is_match_helper(s, p, i, j, s_len, p_len, memo) when j == p_len do
    i == s_len
  end

  defp is_match_helper(s, p, i, j, s_len, p_len, memo) do
    case :ets.lookup(memo, {i, j}) do
      [{_, result}] -> result
      [] ->
        first_match = i < s_len and (String.at(s, i) == String.at(p, j) or String.at(p, j) == ".")

        result =
          if j + 1 < p_len and String.at(p, j + 1) == "*" do
            is_match_helper(s, p, i, j + 2, s_len, p_len, memo) or
              (first_match and is_match_helper(s, p, i + 1, j, s_len, p_len, memo))
          else
            first_match and is_match_helper(s, p, i + 1, j + 1, s_len, p_len, memo)
          end

        :ets.insert(memo, {{i, j}, result})
        result
    end
  end
end
