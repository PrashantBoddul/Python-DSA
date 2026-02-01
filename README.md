# Quick Sort Algorithm (Partition Logic)

## Goal
The goal is to sort an unsorted array (e.g., `[0,10,1,9,2,8,3,7,4,6,5]`) into ascending order using **Quick Sort** with the **Partition Logic** approach.

---

## How It Works
- The algorithm selects a **pivot element** (here, the last element of the current subarray).
- It partitions the array into two parts:
  - Elements smaller than or equal to the pivot.
  - Elements greater than the pivot.
- The pivot is placed in its correct position after partitioning.
- Recursively applies Quick Sort to the left and right subarrays until the entire array is sorted.

---

## Sample Output
- Original Array :- [0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
- New Partition Range: [0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5] (Pivot: 5) --- Swap: arr[Looks like the result wasn't safe to show. Let's switch things up and try something else!] with arr[Looks like the result wasn't safe to show. Let's switch things up and try something else!] Current state: [0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5] Skip: 10 is larger than 5 Swap: arr[Looks like the result wasn't safe to show. Let's switch things up and try something else!] with arr[Looks like the result wasn't safe to show. Let's switch things up and try something else!] Current state: [0, 1, 10, 9, 2, 8, 3, 7, 4, 6, 5] ...
- Final Swap: Pivot 5 moves to index 5 Partition Result: [0, 1, 2, 3, 4, 5, 9, 7, 10, 6, 8]
- Fully Sorted Shelf: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


---

## Complexity
- **Best Case:** O(n log n) → Balanced partitions.
- **Worst Case:** O(n²) → Poor pivot choice (e.g., always smallest/largest element).
- **Average Case:** O(n log n)
- **Space Complexity:** O(log n) → Due to recursive calls.

---

## Use Cases
- Efficient sorting for large datasets.
- Commonly used in system libraries and competitive programming.
- Foundation for advanced algorithms like randomized Quick Sort.
