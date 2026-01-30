# Merge Sort Algorithm (Recursion)

## Goal
The goal is to sort an unsorted array (e.g., `[1,9,2,8,3,7,4,6,5,10,0]`) into ascending order using **Merge Sort**, a divide‑and‑conquer algorithm that relies on recursion.

---

## How It Works
- The array is recursively divided into two halves until each subarray has one element.
- The **Merge** function then combines these sorted halves:
- It compares elements from both halves.
- The smaller element is appended to the result array.
- Remaining elements are added once one half is exhausted.
- This process continues until the entire array is merged back into a sorted sequence.

---

## Sample Output
- Original Array :- [1, 9, 2, 8, 3, 7, 4, 6, 5, 10, 0]
- During Merge Steps (partial outputs): [1] [1, 9] [2] [2, 8] [1, 2, 8, 9] ...
- Final Sorted Array :- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

---

## Complexity
- **Best Case:** O(n log n)
- **Worst Case:** O(n log n)
- **Average Case:** O(n log n)
- **Space Complexity:** O(n) → Extra space required for merging.

---

## Use Cases
- Sorting large datasets efficiently.
- Preferred when stability (preserving order of equal elements) is required.
- Foundation for advanced algorithms in data processing and parallel computing.
