# Binary Search Algorithm

## Goal
The goal is to find the position of a given card (e.g., `5`) by turning the minimum number of cards, using **Binary Search**.

---

## How It Works
- The user inputs the card they want to search for.
- The algorithm repeatedly divides the deck into halves:
- It checks the middle card.
- If the middle card matches, the search ends.
- If the middle card is greater, the search continues in the left half.
- If the middle card is smaller, the search continues in the right half.
- Once the card is found, it prints:
- The number of iterations taken
- The position of the card in the deck (0‑indexed and human‑friendly)
- If the card is not found, the program notifies the user.

---

- Cards:- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- Enter Card Which You Want To Test :- 5
- Found at Iteration :- 3 
- Position of Card :- 4


---

## Complexity
- **Best Case:** O(1) → Card found at the middle position.
- **Worst Case:** O(log n) → Card found after repeatedly halving the deck.
- **Space Complexity:** O(1)

---

## Use Cases
- Searching in sorted datasets.
- Efficient lookups in large arrays.
- Foundation for advanced algorithms like binary search trees.

