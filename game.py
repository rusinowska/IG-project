"""
Red7
made by Zofia Rusinowska
"""
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indygo', 'violet']
numbers = [1, 2, 3, 4, 5, 6, 7]
cards = []
user = []
hand_one = []
hand_two = []
palette_one = []
palette_two = []
background = [(0, 'red')]
pile = []
active_rule = 'red'
chosen_action =  None


def generate_cards(*colors, *numbers, *cards):
    """
    Funkcja generuje karty
    """
    for c in colors:
        for n in numbers:
            cards.append(c,n)

def generate_hand(hand, cards):
    """
    Funkcja losuje 7 dla gracza
    """
    counter = 7
    for counter > 0:
        card = random.choice(hand)
        #usuń z cards daną kartę
        hand.append(card)
        counter-=1
    return hand

def get_pile(cards):
    pile = cards

def action(*hand, *palette, *pile, chosen_action):
    if len(hand) > 0:
        choose_action(hand, palette, pile, chosen_action)

def choose_action(*hand, *palette, *pile, chosen_action):
    """
    Funkcja pozwala na wybor rodzaju ruchu
    """
    if chosen_action == 0:
        return put_in_palette(hand, palette)
    elif chosen_action == 1:
        return put_in_background(hand, background)
    elif chosen_action == 2:
        return get_from_pile(hand, pile) && put_in_background()

def get_from_pile(*hand, *pile):
    """
    Funkcja pobiera kartę z wierzchu stosu
    """
    new_card = pile.pop(last)
    hand.append(new_card)
    return new_card

def put_in_palette(*hand, *palette, chosen_card):
    """
    Funkcja pozwala wyłozyc jedna karte do palety
    """
    hand.pop(chosen_card)

def put_in_background(*hand, *background, chosen_card):
    """
    Funkcja pozwala wyłozyc jedna karte na tło
    """
    new_card = hand.pop(chosen_card)
    background.append(new_card)
    return new_card


def check_if_win(rule, *palette_one, *palette_two):
    """
    Funkcja sprawdza w czy w danej regule ręka gracza wygrywa
    """
    points_one = count_points(rule, palette_one)
    points_two = count_points(rule, palette_two)

    if poonts_one > ponits_two:
        return True
    else:
        return False


def count_points(rule, *palette):
    """
    Funkcja sprawdza w czy w danej regule ręka gracza wygrywa
    """
    a = 0
    if rule == 'red':
        for c in palette:
            if c > a:
                a = class

    elif rule == 'orange':
        #wygrywa najwięcej kart z tymi samymi liczbami
        #sort po 1. argumencie
        sorted(palette)
        b = [1]
        n = 0
        last = 0
        for c in palette:
            if c == last:
                b+=1
            else:
                last = c


    elif rule == 'yellow':
        #wygrywa najwięcej kart tego samego koloru
        #sort po 2. argumencie

    elif rule == 'green':
        for c in palette:
            if c%2 == 0:
                a+=1

    elif rule == 'blue':
        #wygrywa najwięcej kart w różnych kolorach
        colors = []
        for c in palette:
            if  c[1] in colors == True: #????????
                colors.append(c[1])
                a+=1

    elif rule == 'indygo':
        #wygrywa najwięcej kart z kolejnymi liczbami
        #sort po 1. argumencie

    elif rule == 'violet':
        for c in palette:
            if c < 4:
                a+=1
    return a
