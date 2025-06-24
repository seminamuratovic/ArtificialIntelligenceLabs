/* 
Representation:
% z     - represents 0
% s(N)  - represents successor, so s(z) is 1, s(s(z)) is 2, etc.
*/

/* 
--- Addition --- 
% peano_add(X, Y, Z) means X + Y = Z
*/
peano_add(z, N, N).
peano_add(s(M), N, s(R)) :-
    peano_add(M, N, R).

/* 
--- Subtraction --- 
% peano_sub(X, Y, Z) means X - Y = Z (fails if Y > X)
*/
peano_sub(N, z, N).
peano_sub(s(N), s(M), R) :-
    peano_sub(N, M, R).

/* 
--- Multiplication ---
% peano_mul(X, Y, Z) means X * Y = Z
*/ 
peano_mul(z, _, z).
peano_mul(s(N), M, R) :-
    peano_mul(N, M, R1),
    peano_add(M, R1, R).

/* 
--- Division ---
% peano_div(N, M, Q) means N // M = Q (integer division)
*/
% If N < M, then N div M = 0
peano_div(N, M, z) :-
    less_than(N, M).

% If N >= M, subtract and recurse
peano_div(N, M, s(Q)) :-
    peano_sub(N, M, R),
    peano_div(R, M, Q).

/* --- Helper: less_than(A, B) is true if A < B */
less_than(z, s(_)).
less_than(s(N), s(M)) :-
    less_than(N, M).

/* --- Integer to Peano conversion ---*/
int_to_peano(0, z).
int_to_peano(N, s(P)) :-
    N > 0,
    N1 is N - 1,
    int_to_peano(N1, P).

/* --- Peano to Integer conversion ---*/
peano_to_int(z, 0).
peano_to_int(s(N), X) :-
    peano_to_int(N, X1),
    X is X1 + 1.
