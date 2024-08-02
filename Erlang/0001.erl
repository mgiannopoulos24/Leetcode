-spec two_sum(Nums :: [integer()], Target :: integer()) -> [integer()].
two_sum(Nums, Target) ->
    two_sum(Nums, Target, 0, dict:new()).

two_sum([], _Target, _Index, _Dict) ->
    []; % This case should never be hit due to the problem constraints
two_sum([H | T], Target, Index, Dict) ->
    case dict:find(Target - H, Dict) of
        {ok, FoundIndex} ->
            [FoundIndex, Index];
        error ->
            two_sum(T, Target, Index + 1, dict:store(H, Index, Dict))
    end.
