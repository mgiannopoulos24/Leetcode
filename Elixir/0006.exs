defmodule Solution do
  @spec convert(s :: String.t(), num_rows :: integer()) :: String.t()
  def convert(s, num_rows) do
    length = String.length(s)

    # Handle edge cases where no zigzag conversion is needed
    if num_rows == 1 or num_rows >= length do
      s
    else
      # Initialize a list of empty strings for each row
      rows = List.duplicate("", num_rows)
      
      # Start processing characters
      build_rows(String.graphemes(s), rows, num_rows, 0, false)
      |> Enum.join("")
    end
  end

  defp build_rows([], rows, _num_rows, _current_row, _going_down) do
    rows
  end

  defp build_rows([char | rest], rows, num_rows, current_row, going_down) do
    # Update the row with the current character
    updated_rows = List.update_at(rows, current_row, &(&1 <> char))
    
    # Determine the new direction and next row
    new_going_down =
      if current_row == 0 or current_row == num_rows - 1 do
        not going_down
      else
        going_down
      end

    next_row = if new_going_down, do: current_row + 1, else: current_row - 1

    # Recursively process the remaining characters
    build_rows(rest, updated_rows, num_rows, next_row, new_going_down)
  end
end
