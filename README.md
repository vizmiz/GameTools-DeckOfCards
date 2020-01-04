# GameTools-DeckOfCards
Returns a list that contains a shuffled 52 count deck of playing cards. No Jokers


.DealDeck() Is the only thing it has to offer. returning a pre-shuffles deck of cards as a list.

*Content Example*:
```
['K♦', '3♥', '4♠', 'J♣', '2♣', '3♠', '9♥', '8♠', '9♦', '3♦', '8♣', 'Q♦', '2♦', '8♦', '6♠', '2♠', 'A♠', 'Q♣', '9♠', '5♥', '10♣', '6♦', 'K♠', '7♠', '8♥', '2♥', 'K♣', '5♦', '4♣', '6♥', '4♦', '6♣', '7♥', '5♣', 'J♦', 'A♥', '10♥', '7♣', 'J♠', 'A♦', 'Q♠', '10♠', 'Q♥', '3♣', 'J♥', '9♣', '7♦', '4♥', '10♦', '5♠', 'A♣', 'K♥']
```



*Example Code*:

```py
import DeckOfCards

DD=DeckOfCards.DealDeck()

for each in DD:
    print(each)
```

>>> 3♣
3♠
J♥
K♦
2♣
6♦
9♣
6♥
Q♠
5♥
8♥
A♥
7♠
Q♣
7♦
J♦
6♣
A♣
A♦
Q♥
8♠
2♠
4♦
7♥
4♠
9♦
10♦
5♣
J♠
A♠
J♣
10♣
K♣
K♠
3♥
2♦
5♦
4♥
4♣
2♥
5♠
6♠
8♦
10♠
K♥
9♥
7♣
3♦
8♣
9♠
Q♦
10♥
