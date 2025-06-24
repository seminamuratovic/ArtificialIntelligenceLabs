/* LAB 2: Bird Identification Expert System */

:- dynamic known/2.

reset :- retractall(known(_, _)).

ask(Attribute, Value) :-
    known(Attribute, Value), !.
ask(Attribute, _) :-
    known(Attribute, _), !, fail.
ask(Attribute, Value) :-
    format('What is the ~w? ', [Attribute]),
    read(UserInput),
    asserta(known(Attribute, UserInput)),
    UserInput = Value.

/* % Bird rules */
bird(laysan_albatross) :-
    family(albatross),
    color(white),
    location(pacific).

bird(black_footed_albatross) :-
    family(albatross),
    color(dark),
    location(pacific).

bird(trumpeter_swan) :-
    family(swan),
    color(white),
    sound(trumpeting).

/* % Added Bird: European Robin */
bird(european_robin) :-
    family(passerine),
    color(orange_breast),
    location(europe),
    sound(song).

/* % Family and order hierarchy */
family(albatross) :- order(tubenose).
family(swan) :- order(waterfowl).
family(passerine) :- order(perching).

order(tubenose) :- nostrils(external_tubular), live(at_sea), bill(hooked).
order(waterfowl) :- feet(webbed), bill(flat), neck(long).
order(perching) :- feet(perching), bill(thin), neck(short).

/* % Askable predicates */
color(X) :- ask(color, X).
location(X) :- ask(location, X).
sound(X) :- ask(sound, X).
nostrils(X) :- ask(nostrils, X).
live(X) :- ask(live, X).
bill(X) :- ask(bill, X).
feet(X) :- ask(feet, X).
neck(X) :- ask(neck, X).

/* Prompts to Run in SWISH for LAB 2 */

?- reset, bird(B).               
?- trace, bird(B).      
?- trace, color(orange_breast).  
?- findall(B, bird(B), List).    
?- setof(B, bird(B), Set).     