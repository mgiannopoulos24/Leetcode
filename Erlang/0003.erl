-export([length_of_longest_substring/1]).

-spec length_of_longest_substring(S :: unicode:unicode_binary()) -> integer().
length_of_longest_substring(S) ->
    length_of_longest_substring(S, 0, 0, 0, #{}).

-spec length_of_longest_substring(S :: unicode:unicode_binary(), Left :: integer(), Right :: integer(), MaxLength :: integer(), CharMap :: #{}) -> integer().
length_of_longest_substring(<<>>, _Left, _Right, MaxLength, _CharMap) ->
    MaxLength;
length_of_longest_substring(S, Left, Right, MaxLength, CharMap) ->
    <<CurrentChar:8, Rest/binary>> = S,
    case maps:get(CurrentChar, CharMap, -1) of
        LastIndex when LastIndex >= Left ->
            NewLeft = LastIndex + 1,
            NewCharMap = maps:put(CurrentChar, Right, CharMap),
            length_of_longest_substring(Rest, NewLeft, Right + 1, MaxLength, NewCharMap);
        _ ->
            NewCharMap = maps:put(CurrentChar, Right, CharMap),
            NewMaxLength = max(MaxLength, Right - Left + 1),
            length_of_longest_substring(Rest, Left, Right + 1, NewMaxLength, NewCharMap)
    end.

max(A, B) when A > B -> A;
max(_A, B) -> B.
