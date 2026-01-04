# Linear Rotated Search Algorithm

## Goal
The goal is to find the position of a given card (e.g., `5`) in a **rotated deck** by turning the minimum number of cards, using **Linear Rotated Search**.

---

## How It Works
- The deck is rotated (e.g., `[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]`).
- The user inputs the card they want to search for.
- The algorithm checks each card sequentially from left to right.
- Once the card is found, it prints:
- The number of cards turned
- The position of the card in the deck (0‑indexed and human‑friendly)
- If the card is not found, the program notifies the user.

---

## Sample Output
- Cards:- [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
- Enter Card Which You Want To Test :- 5 8 5 9 5 10 5 1 5 2 5 3 5 4 5 5 5
- Number of Cards Turned By Using Linear Rotated Search Algorithm :- 8 
- Position of Card '5' By Using Linear Rotated Search Algorithm :- 7



---

## Complexity
- **Best Case:** O(1) → Card found at the first position.
- **Worst Case:** O(n) → Card found at the last position or not present.
- **Space Complexity:** O(1)

---

## Use Cases
- Searching in rotated arrays (common in interview problems).
- Handling datasets that are partially sorted but rotated.
- Educational demonstrations of search algorithms in non‑sorted sequences.
