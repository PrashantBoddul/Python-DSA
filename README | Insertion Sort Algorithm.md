# 📝 Insertion Sort Algorithm

## 🎯 Goal
The goal is to sort an unsorted array (e.g., `[1,9,2,8,3,7,4,6,5,10,0]`) into ascending order using **Insertion Sort**.

---

## 🧠 How It Works
- The algorithm builds the sorted array one element at a time.
- It picks the next element and compares it with elements in the sorted portion.
- If the element is smaller, it shifts larger elements one position to the right.
- The element is then inserted into its correct position.
- This process continues until the entire array is sorted.

---

## 📦 Sample Output
- Original Array :- [1, 9, 2, 8, 3, 7, 4, 6, 5, 10, 0]
- Original Array After Sorting :- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


---

## ⚡ Complexity
- **Best Case:** O(n) → Already sorted array.
- **Worst Case:** O(n²) → Completely unsorted array.
- **Average Case:** O(n²)
- **Space Complexity:** O(1)

---

## 📚 Use Cases
- Sorting small datasets efficiently.
- Useful when the array is already partially sorted.
- Commonly used in educational demonstrations of sorting algorithms.
