/*LAB 1: Logic Programming with Allat */

/*% 1. Basic Facts*/
parent(mary, john).
parent(john, alice).
parent(alice, elsa).

/*% 2. Rule: Grandparent*/
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

/*% 3. Recursive: Largest Element in a List*/
largest_element(X, [X]).
largest_element(X, [X|Rest]) :-
    largest_element(Y, Rest),
    X >= Y.
largest_element(Y, [X|Rest]) :-
    largest_element(Y, Rest),
    Y > X.

/*% 4. Recursive: Length of a List*/
length_list([], 0).
length_list([_|T], N) :-
    length_list(T, N1),
    N is N1 + 1.

/*% 5. Recursive: Factorial*/
factorial(0, 1).
factorial(N, F) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.

/*% 6. Backtracking: Multiple Solutions*/
likes(mary, pizza).
likes(mary, sushi).
likes(john, burger).

/*Prompts to Run in SWISH for LAB 1*/

?- grandparent(mary, X).
?- largest_element(Max, [3, 8, 5, 1]).
?- length_list([a, b, c, d], L).
?- factorial(5, F).
?- likes(mary, Food).
?- trace.
?- factorial(3, F).