----------------- Step by Step in details -----------------


    I - [INIT LIST CONST] - initialise 2 const for my families ("Color") and for my values ("1-13").

    II - [INIT CLASS CARD] - create a class "Card" and init 2 attributes ("family" , "value").

    III - [LINK LIST CONST -> CLASS ATTR] -
        - return with "__str__" function 
        - (self.value , const_of_families[self.family]).
        -> (Optionnal) in test.py check "Test creation card"

    IV - [INIT CLASS DECK] - create a class "Deck" with self attribute,
                           - init a empty list "cards" , 
                           - for color (4 in this fact) and for value (14 in fact)
                                                                    {index start in 0}
                           - i create var "card" for contain "Card(color , value)".
                           - append my "card" in my list "cards".
                           -> (Optionnal) in test.py check "Test render deck".

    V - [RENDER DECK] - create "__init__" function with self attribute 
                      - init a empty list "render_deck".
                      - for card "in self.cards" 
                      - i append my list in my "card" with a stringification.
                      -> (Display) i return a "\n" and a join this with my list render_deck

    VI - [ADD / POP / SHUFFLE] - function "pop_card" with self attribute
                               - return "self.cards.pop()"
                               - function "append_card" with self and card attribute
                               - append "self.card.append(card)"
                               - function "shuffle_card" with self attribute
                               - shuffle "(self.cards)"
    
    VII - [COMPARE CARDS] - create function "__lt__" in "Card" class with self and other attribute
                          - return "self.value < other.value"
                          - if the condition is "True" or "False" the result append in the console.
                          -> (Optionnal) in test.py check "Test compare cards".
                               
    
          


----------------- Initialise Game -----------------


    First Step : 
    - Initialise card deck and shuffle function. --> "Check"

    Second Step : 
    - Comparate cards. --> "Check"

    Third Step : 
    - Show the deck content. --> "Check"
    - Show "King , Jack and Queen" for my 11 , 12 , 13 values.

    Four Step : 
    - (Move cards ?).
    - Initialise turn and input for hand of all players on the board.

    Five Step : 
    - Initialise a hand with (inheritance) ?


---------------- Operating function ----------------


    For the operating rules : 
    - First -> the HiLo system with +1 / 0 / -1.
    - Second -> reach on the net for method plus / minus.
