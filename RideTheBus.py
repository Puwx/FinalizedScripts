import random

suits = ["Hearts","Diamonds","Clubs","Spades"]

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
        if self.suit == "Hearts" or self.suit =="Diamonds":
            self.colour = "Red"
        else:
            self.colour = "Black"
        if self.value <= 10 and self.value != 1:
            self.name = str(value)
        else:
            if self.value == 1:
                self.name = "Ace"
            elif self.value == 11:
                self.name = "Jack"
            elif self.value == 12:
                self.name = "Queen"
            else:
                self.name ="King"
    def __str__(self):
        return "{} of {}".format(self.name,self.suit)

def card_values():
    values = []
    for value in range(1,14):
        for suit in suits:
            values.append((suit,value))
    return values

def build_deck(card_vals):
    cards =[]
    for suit,val in card_vals:
        card = Card(suit,val)
        cards.append(card)
    return cards

def pick_card(deck):
    length = len(deck)
    card_pos = random.randint(0,length)
    current_card = deck[card_pos]
    deck.pop(card_pos)
    return current_card

values = card_values()

built_deck = build_deck(values)

def red_or_black():
    r_o_b_q = input("Red or black?")
    if r_o_b_q.lower() == "red" or r_o_b_q.lower() == "black":
        r_o_b = pick_card(built_deck)
        if r_o_b_q.lower() == r_o_b.colour.lower():
            print("Right answer! The card was the {}.".format(r_o_b))
            return r_o_b
        else:
            print("Wrong answer! The card was the {}.".format(r_o_b))

    else:
        print("Please provide a valid input, either Red or Black.")

def high_or_low(r_b_card):
    h_o_l_q = input("High or low?").lower()
    if h_o_l_q == "high" or h_o_l_q == "low":
        h_o_l = pick_card(built_deck)
        hl = None
        if h_o_l.value < r_b_card.value:
            hl = "Low"
        elif h_o_l.value > r_b_card.value:
            hl = "High"
        else:
            hl = "Equal"
        print(hl)
        if h_o_l_q.lower() == hl.lower():
            print ("That's the right anwswer! The card that was drawn was {}.".format(h_o_l))
            return h_o_l
        elif h_o_l_q.lower() != hl.lower():
            print("That's the wrong- anwswer! The card that was drawn was {}.".format(h_o_l))
        elif hl == "Equal":
            print ("Those cards have equal value! The card that was drawn was {}.".format(h_o_l))
    else:
        print("That is not a valid answer, please input either high or low.")

def in_or_out(r_b_card,h_l_card):
    i_o_o_q = input("In between(In) outside(Out)?").lower()
    if i_o_o_q == "in" or i_o_o_q == "out":

        i_o_o = pick_card(built_deck)
        high_card = max(r_b_card.value,h_l_card.value)
        low_card = min(r_b_card.value,h_l_card.value)
        print("Max card: {} Min card: {}".format(high_card,low_card))

        if (i_o_o.value < high_card and i_o_o.value > low_card) and (i_o_o_q == "in"):
            print("Thats the right answer! The card that was drawn was {}.".format(i_o_o))
            return i_o_o 

        elif (i_o_o.value < low_card and i_o_o.value > high_card)and (i_o_o_q == "out"):
            print("Thats the right answer! The card that was drawn was {}.".format(i_o_o))
            return i_o_o

        elif (i_o_o.value == high_card) or (i_o_o.value == low_card):
            print("The card that was drawn ({}), has an equal value to a previous card.".format(i_o_o))

        else:
            print("Wrong answer! The card that was drawn ({}) was not the same as you specified.".format(i_o_o))
    else:
        print("Invalid answer, please specify either in or out.")

def suit_guess():
    s_g_q = input("What suit do you think the next card will be ?(Clubs,Spades, Diamonds, or Hearts)  ").lower()
    if s_g_q in ("hearts","diamonds","spades","clubs"):
        s_g = pick_card(built_deck)
        if s_g_q == s_g.suit:
            print("That's the right answer! The card that was drawn was {}.".format(s_g)) 
            print("Congratulations you've won the game!")
            return s_g
        else:
            print ("The suit that you guessed does not match the card that was drawn ({}).".format(s_g))
    else:
        print ("Please provide a valid answer, a suit of card must be specified.")



if len(built_deck) > 0:
    while True:
        rb = red_or_black()
        if rb:
            hl = high_or_low(rb)
            if hl:
                io  = in_or_out(rb,hl)
                if io:
                    sg = suit_guess()
                    if sg:
                        print("You've won the game! Thanks for playing!")
            
else:
    print("You are out of cards! You aren't very good at this.")
