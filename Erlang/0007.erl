-export([reverse/1]).

-spec reverse(X :: integer()) -> integer().
reverse(X) ->
    % Define the 32-bit signed integer range
    MinInt = -2_147_483_648,
    MaxInt = 2_147_483_647,

    % Check if the number is negative
    Negative = X < 0,

    % Work with the absolute value of X
    XAbs = abs(X),

    % Convert to string, reverse, and convert back to integer
    ReversedStr = lists:reverse(integer_to_list(XAbs)),
    ReversedInt = list_to_integer(ReversedStr),

    % Apply the original sign to the reversed integer
    Result = if
        Negative -> -ReversedInt;
        true -> ReversedInt
    end,

    % Check for overflow and return the result
    case Result of
        Result when Result < MinInt; Result > MaxInt -> 0;
        _ -> Result
    end.
