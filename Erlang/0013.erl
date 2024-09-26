-spec roman_to_int(S :: unicode:unicode_binary()) -> integer().
roman_to_int(S) ->
    RomanMap = #{
        <<"I">> => 1,
        <<"V">> => 5,
        <<"X">> => 10,
        <<"L">> => 50,
        <<"C">> => 100,
        <<"D">> => 500,
        <<"M">> => 1000
    },
    
    RomanChars = unicode:characters_to_list(S),
    {Total, _PrevValue} = lists:foldl(fun(Char, {Total, PrevValue}) ->
        CharBin = <<Char/utf8>>, % Convert the integer to a binary string
        CurrentValue = maps:get(CharBin, RomanMap),
        if
            CurrentValue < PrevValue -> {Total - CurrentValue, CurrentValue};
            true -> {Total + CurrentValue, CurrentValue}
        end
    end, {0, 0}, lists:reverse(RomanChars)),
    
    Total.
