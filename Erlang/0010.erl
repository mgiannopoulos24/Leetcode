-export([is_match/2]).

-spec is_match(S :: unicode:unicode_binary(), P :: unicode:unicode_binary()) -> boolean().
is_match(S, P) ->
    Memo = ets:new(memo, [set, public, named_table]),
    Result = is_match_helper(S, P, 0, 0, byte_size(S), byte_size(P), Memo),
    ets:delete(Memo),
    Result.

-spec is_match_helper(S :: unicode:unicode_binary(), P :: unicode:unicode_binary(), I :: integer(), J :: integer(), SLen :: integer(), PLen :: integer(), Memo :: ets:tid()) -> boolean().
is_match_helper(_, _, I, J, SLen, PLen, _) when J == PLen ->
    I == SLen;
is_match_helper(S, P, I, J, SLen, PLen, Memo) ->
    case ets:lookup(Memo, {I, J}) of
        [{_, Result}] -> Result;
        [] ->
            FirstMatch = I < SLen andalso
                         (binary:at(S, I) =:= binary:at(P, J) orelse binary:at(P, J) =:= $.),
            IsStar = J + 1 < PLen andalso is_star(P, J + 1),
            Result = if
                IsStar ->
                    is_match_helper(S, P, I, J + 2, SLen, PLen, Memo) orelse
                    (FirstMatch andalso is_match_helper(S, P, I + 1, J, SLen, PLen, Memo));
                true ->
                    FirstMatch andalso is_match_helper(S, P, I + 1, J + 1, SLen, PLen, Memo)
            end,
            ets:insert(Memo, {{I, J}, Result}),
            Result
    end.

is_star(P, Index) ->
    binary:at(P, Index) =:= $*.