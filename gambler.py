#Gambler.py Version 1.0
#A Library By Matthew Zenn
#https://github.com/MatthewZenn

import random
import os

deck = ["ace hearts", "two hearts", "three hearts", "four hearts", "five hearts", "six hearts", "seven hearts", "eight hearts", "nine hearts", "ten hearts", "jack hearts", "queen hearts", "king hearts"
, "ace clubs", "two clubs", "three clubs", "four clubs", "five clubs", "six clubs", "seven clubs", "eight clubs", "nine clubs", "ten clubs", "jack clubs", "queen clubs", "king clubs"
, "king diamonds", "queen diamonds", "jack diamonds", "ten diamonds", "nine diamonds", "eight diamonds", "seven diamonds", "six diamonds", "five diamonds", "four diamonds", "three diamonds", "two diamonds", "ace diamonds"
, "king spades", "queen spades", "jack spades", "ten spades",  "nine spades", "eight spades", "seven spades", "six spades", "five spades", "four spades", "three spades", "two spades", "ace spades"]

stack = list(deck)
pile = []
myhand = []
yourhand = []

print(stack)

def reset():
    global stack
    stack = list(deck)
    del myhand[:]
    del yourhand[:]
    del pile[:]
    os.system('cls')
    print(stack)

def mix(number):
    for i in range(number):
        random.shuffle(stack)
    print(stack)

def cull(card,p,u):
    print(card)
    p.append(card)
    u.remove(card)
    print()
    print(u)
    
def deal(amount):
    for i in range(amount):
        myhand.append(stack[0])
        print(stack[0])
        stack.pop(0)
        yourhand.append(stack[0])
        print(stack[0])
        stack.pop(0)
    print()
    print(stack)

def hit(player,o):
    player.append(o[0])
    print(o[0])
    o.pop(0)
    print()
    print(o)

def throw(card,f):
    print(card)
    pile.insert(0,card)
    f.remove(card)
    print()
    print(pile)


def clean():
    os.system('cls')
    print(stack)

def show(q):
    print(q)