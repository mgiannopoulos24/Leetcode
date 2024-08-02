%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec add_two_numbers(L1 :: #list_node{} | null, L2 :: #list_node{} | null) -> #list_node{} | null.
add_two_numbers(L1, L2) ->
    add_two_numbers(L1, L2, 0).

-spec add_two_numbers(L1 :: #list_node{} | null, L2 :: #list_node{} | null, Carry :: integer()) -> #list_node{} | null.
add_two_numbers(null, null, 0) ->
    null;
add_two_numbers(null, null, Carry) when Carry > 0 ->
    #list_node{val = Carry, next = null};
add_two_numbers(L1, null, Carry) ->
    add_two_numbers(L1, #list_node{val = 0, next = null}, Carry);
add_two_numbers(null, L2, Carry) ->
    add_two_numbers(#list_node{val = 0, next = null}, L2, Carry);
add_two_numbers(#list_node{val = Val1, next = Next1}, #list_node{val = Val2, next = Next2}, Carry) ->
    Sum = Val1 + Val2 + Carry,
    NewVal = Sum rem 10,
    NewCarry = Sum div 10,
    #list_node{val = NewVal, next = add_two_numbers(Next1, Next2, NewCarry)}.