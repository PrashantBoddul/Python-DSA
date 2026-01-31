# Quick Sort Algorithm (Recursion)

## Goal
The goal is to sort an unsorted array (e.g., `[1,9,2,8,3,7,4,6,5,10,0]`) into ascending order using **Quick Sort**, a divide‑and‑conquer algorithm that relies on recursion.

---

## How It Works
- The algorithm selects a **pivot element** (in this case, the middle element).
- It partitions the array into three parts:
  - **Left** → Elements smaller than the pivot.
  - **MidVal** → Elements equal to the pivot.
  - **Right** → Elements greater than the pivot.
- Recursively applies Quick Sort to the left and right partitions.
- Combines results: `Quick_Sort(Left) + MidVal + Quick_Sort(Right)`.

---

## Sample Output
- Original Array :- [1, 9, 2, 8, 3, 7, 4, 6, 5, 10, 0]
- During Partition Steps: [1, 2, 8, 3, 7, 4, 6, 5, 0] [9] [10] [1, 2, 3, 7, 4, 6, 5, 0] [8] [] ...
- Final Sorted Array :- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


---

## Complexity
- **Best Case:** O(n log n) → Balanced partitions.
- **Worst Case:** O(n²) → Poor pivot choice (e.g., always smallest/largest element).
- **Average Case:** O(n log n)
- **Space Complexity:** O(log n) → Due to recursive calls.

---

## Use Cases
- Efficient sorting for large datasets.
- Commonly used in competitive programming and system libraries.
- Foundation for advanced algorithms like randomized Quick Sort.
