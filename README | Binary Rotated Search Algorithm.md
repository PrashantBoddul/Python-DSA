# Binary Search in Rotated Array

## Goal
  The goal is to find the position of a given card (e.g., `10`) in a **rotated deck** using **Binary Search**. Unlike linear search, this algorithm leverages the sorted property of subarrays even after rotation.

---

## How It Works
- The deck is rotated (e.g., `[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]`).
- The user specifies the card they want to search for.
- The algorithm repeatedly divides the deck into halves:
- It checks the middle card.
- If the middle card matches, the search ends.
- If the right half is sorted, the algorithm decides whether to search there.
- If the left half is sorted, the algorithm decides whether to search there.
- Once the card is found, it prints:
- The number of iterations taken
- The position of the card in the deck (0‑indexed and human‑friendly)
- If the card is not found, the program notifies the user.

---

## Sample Output
- Cards:- [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
- Enter Card Which You Want To Test :- 10
- Found At Iteration 1

---

## Complexity
- **Best Case:** O(1) → Card found at the middle position.
- **Worst Case:** O(log n) → Card found after repeatedly halving the rotated deck.
- **Space Complexity:** O(1)

---

## Use Cases
- Searching in rotated sorted arrays (common in coding interviews).
- Efficient lookups in datasets that are sorted but rotated due to shifts.
- Foundation for advanced problems like “Search in Rotated Sorted Array” on LeetCode.
