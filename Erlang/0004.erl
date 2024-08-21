-spec find_median_sorted_arrays(Nums1 :: [integer()], Nums2 :: [integer()]) -> float().
find_median_sorted_arrays(Nums1, Nums2) ->
    case length(Nums1) > length(Nums2) of
        true -> find_median_sorted_arrays(Nums2, Nums1);
        false ->
            X = length(Nums1),
            Y = length(Nums2),
            find_median(Nums1, Nums2, X, Y, 0, X)
    end.

-spec find_median(Nums1 :: [integer()], Nums2 :: [integer()], X :: integer(), Y :: integer(), Low :: integer(), High :: integer()) -> float().
find_median(Nums1, Nums2, X, Y, Low, High) when Low =< High ->
    PartitionX = (Low + High) div 2,
    PartitionY = (X + Y + 1) div 2 - PartitionX,

    MaxLeftX = if PartitionX =:= 0 -> -1000000000; true -> lists:nth(PartitionX, Nums1) end,
    MinRightX = if PartitionX =:= X -> 1000000000; true -> lists:nth(PartitionX + 1, Nums1) end,

    MaxLeftY = if PartitionY =:= 0 -> -1000000000; true -> lists:nth(PartitionY, Nums2) end,
    MinRightY = if PartitionY =:= Y -> 1000000000; true -> lists:nth(PartitionY + 1, Nums2) end,

    case MaxLeftX =< MinRightY andalso MaxLeftY =< MinRightX of
        true ->
            if (X + Y) rem 2 =:= 0 ->
                (max(MaxLeftX, MaxLeftY) + min(MinRightX, MinRightY)) / 2.0;
            true ->
                max(MaxLeftX, MaxLeftY)
            end;
        false ->
            if MaxLeftX > MinRightY ->
                find_median(Nums1, Nums2, X, Y, Low, PartitionX - 1);
            true ->
                find_median(Nums1, Nums2, X, Y, PartitionX + 1, High)
            end
    end;

find_median(_, _, _, _, _, _) ->
    erlang:error(invalid_argument).
