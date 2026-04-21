import tkinter as tk
from time import perf_counter_ns

# ---------------- Sorting Algorithms ---------------- #

def lambda_sort(arr):
    return sorted(arr, key=lambda x: x)

def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def cocktail_shaker_sort(arr):
    a = arr[:]
    n = len(a)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False
        for i in range(start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        start += 1

    return a

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

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

    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)

    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

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

def bucket_sort(arr):
    # Simple string-based bucket by first letter
    buckets = {}
    for word in arr:
        key = word[0] if word else ''
        buckets.setdefault(key, []).append(word)

    result = []
    for key in sorted(buckets.keys()):
        result.extend(sorted(buckets[key]))
    return result

# ---------------- Benchmark ---------------- #

def measure_time(func, arr):
    start = perf_counter_ns()
    func(arr)
    end = perf_counter_ns()
    return end - start

# ---------------- GUI Logic ---------------- #

def run_sort(reverse=False):
    input_text = entry.get()
    words = input_text.split()

    if not words:
        result_label.config(text="No input provided.")
        return

    sorted_words = sorted(words, reverse=reverse)
    result_label.config(text=" ".join(sorted_words))

    # Benchmark all algorithms
    results = [
        ("Lambda Sort (O(n log n))", measure_time(lambda_sort, words)),
        ("Bubble Sort (O(n^2))", measure_time(bubble_sort, words)),
        ("Cocktail S. Sort (O(n^2))", measure_time(cocktail_shaker_sort, words)),
        ("Heap Sort (O(n log n))", measure_time(heap_sort, words)),
        ("Merge Sort (O(n log n))", measure_time(merge_sort, words)),
        ("Quick Sort (O(n log n))", measure_time(quick_sort, words)),
        ("Bucket Sort (O(n + k))", measure_time(bucket_sort, words)),
    ]

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Algorithm                      Time (ns)\n")
    output_text.insert(tk.END, "-" * 50 + "\n")

    for name, t in results:
        formatted = format_time(t)
        output_text.insert(tk.END, f"{name:<25}      {formatted}\n")

# Helper function to format time in a human-readable way

def format_time(ns):
    seconds = ns // 1_000_000_000
    ns %= 1_000_000_000

    milliseconds = ns // 1_000_000
    ns %= 1_000_000

    microseconds = ns // 1_000
    nanoseconds = ns % 1_000

    return f"{seconds}s:{milliseconds}:{microseconds}:{nanoseconds}ns"
# ---------------- GUI Setup ---------------- #

root = tk.Tk()
root.title("AlphabetSort")
root.geometry("500x400")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=50)
entry.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

btn_az = tk.Button(btn_frame, text="Sort A-Z", command=lambda: run_sort(False))
btn_az.pack(side=tk.LEFT, padx=5)

btn_za = tk.Button(btn_frame, text="Sort Z-A", command=lambda: run_sort(True))
btn_za.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=10)

output_text = tk.Text(root, height=12, width=60)
output_text.pack()

root.mainloop()