# Linear Search on Card Deck

This project demonstrates a simple **Linear Search Algorithm** implemented in Python to find the position of a specific card in a predefined deck.

---

## 🔍 Problem Statement

We have a deck of 13 cards:

```python
["A", "K", "Q", "J", 2, 3, 4, 5, 6, 7, 8, 9, 10]

The goal is to find the position of a given card (e.g., 5) by turning the minimum number of cards, using Linear Search.

🧠 How It Works
- The user inputs the card they want to search for.
- The algorithm checks each card sequentially from left to right.
- Once the card is found, it prints:
- The number of cards turned
- The position of the card in the deck (0‑indexed and human‑friendly)
If the card is not found, the program notifies the user.

📦 Sample Output
Cards:- ['A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10]

Solve The DSA: We have 13 cards. At which position is card 5? You have to check by turning minimum cards.

Enter Card Which You Want To Test :- 5
A 5
K 5
Q 5
J 5
2 5
3 5
4 5
5 5

Number of Cards Turned By Using Linear Search Algorithm :- 8
Position of Card '5' By Using Linear Search Algorithm :- 7
