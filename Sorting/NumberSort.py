import tkinter as tk
from tkinter import filedialog
from time import perf_counter_ns

# ---------------- Parsing ---------------- #

def parse_input(text):
    try:
        return [int(x) for x in text.split()]
    except ValueError:
        return []

# ---------------- Sorting Algorithms ---------------- #

def lambda_sort(arr):
    return sorted(arr)

def bubble_sort_while(arr):
    a = arr[:]
    n = len(a)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
    return a

def bubble_sort_recursive(arr, n=None):
    if n is None:
        arr = arr[:]
        n = len(arr)

    if n == 1:
        return arr

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return bubble_sort_recursive(arr, n - 1)

def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    a = arr[:]
    n = len(a)

    for i in range(n//2 - 1, -1, -1):
        heapify(a, n, i)

    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)

    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

def cycle_sort(arr):
    a = arr[:]
    n = len(a)

    for cycle_start in range(0, n - 1):
        item = a[cycle_start]
        pos = cycle_start

        for i in range(cycle_start + 1, n):
            if a[i] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while item == a[pos]:
            pos += 1

        a[pos], item = item, a[pos]

        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if a[i] < item:
                    pos += 1

            while item == a[pos]:
                pos += 1

            a[pos], item = item, a[pos]

    return a

def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    min_val = min(arr)

    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements

    for num in arr:
        count[num - min_val] += 1

    result = []
    for i, c in enumerate(count):
        result.extend([i + min_val] * c)

    return result

def shell_sort(arr):
    a = arr[:]
    n = len(a)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2

    return a

# ---------------- Timing ---------------- #

def measure(func, arr):
    start = perf_counter_ns()
    func(arr)
    return perf_counter_ns() - start

def format_time(ns):
    s = ns // 1_000_000_000
    ns %= 1_000_000_000
    ms = ns // 1_000_000
    ns %= 1_000_000
    us = ns // 1_000
    ns %= 1_000
    return f"{s}s:{ms}:{us}:{ns}ns"

# ---------------- File Upload ---------------- #

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return

    with open(file_path, "r") as f:
        content = f.read()

        # Replace newlines and tabs with spaces
        cleaned = content.replace("\n", " ").replace("\r", " ").replace("\t", " ")

        entry.delete(0, tk.END)
        entry.insert(0, cleaned)

# ---------------- Main Logic ---------------- #

def run_sort(reverse=False):
    nums = parse_input(entry.get())
    if not nums:
        result_label.config(text="Invalid input")
        return

    sorted_nums = sorted(nums, reverse=reverse)
    result_label.config(text=" ".join(map(str, sorted_nums)))

    algorithms = [
        ("Lambda (O(n log n))", lambda_sort),
        ("Bubble (while loop)", bubble_sort_while),
        ("Bubble (recursive)", bubble_sort_recursive),
        ("Heap (O(n log n))", heap_sort),
        ("Merge (O(n log n))", merge_sort),
        ("Quick (O(n log n))", quick_sort),
        ("Cycle (O(n^2))", cycle_sort),
        ("Counting (O(n + k))", counting_sort),
        ("Shell (O(n^2))", shell_sort),
    ]

    output.delete("1.0", tk.END)
    output.insert(tk.END, "Algorithm                    Time\n")
    output.insert(tk.END, "-"*40 + "\n")

    for name, func in algorithms:
        t = measure(func, nums)
        output.insert(tk.END, f"{name:<20}      {format_time(t)}\n")

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("NumberSort")
root.geometry("520x450")

entry = tk.Entry(root, width=60)
entry.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Load File", command=load_file).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Sort 0-9", command=lambda: run_sort(False)).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Sort 9-0", command=lambda: run_sort(True)).pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=10)

output = tk.Text(root, height=15, width=60)
output.pack()

root.mainloop()