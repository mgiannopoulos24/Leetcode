-spec is_palindrome(X :: integer()) -> boolean().
is_palindrome(X) ->
    % Handle negative numbers and numbers ending in zero (except zero itself)
    if
        X < 0 orelse (X rem 10 =:= 0 andalso X /= 0) ->
            false;
        true ->
            Reversed = reverse_number(X, 0),
            X =:= Reversed
    end.

% Helper function to reverse the number
reverse_number(0, Reversed) ->
    Reversed;
reverse_number(X, Reversed) ->
    Digit = X rem 10,
    NewReversed = Reversed * 10 + Digit,
    reverse_number(X div 10, NewReversed).
