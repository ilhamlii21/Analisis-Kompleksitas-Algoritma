import time
import matplotlib.pyplot as plt
import random
import sys
from tabulate import tabulate  # type: ignore # Impor pustaka tabulate

sys.setrecursionlimit(2000)

class Comic:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def __repr__(self):
        return f"{self.title} ({self.genre})"

def insertion_sort_iterative(comics, key):
    for i in range(1, len(comics)):
        key_item = comics[i]
        j = i - 1
        while j >= 0 and getattr(comics[j], key) > getattr(key_item, key):
            comics[j + 1] = comics[j]
            j -= 1
        comics[j + 1] = key_item

def measure_iterative_sort_time(comics, key):
    start_time = time.time()
    insertion_sort_iterative(comics, key)
    end_time = time.time()
    return end_time - start_time

def binary_search_recursive_with_delay(comics, target, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2

    for _ in range(1000): 
        _ = mid ** 2

    if getattr(comics[mid], key) == target:
        return mid
    elif getattr(comics[mid], key) > target:
        return binary_search_recursive_with_delay(comics, target, key, low, mid - 1)
    else:
        return binary_search_recursive_with_delay(comics, target, key, mid + 1, high)

def measure_recursive_search_time_with_variation(comics, key, repetitions=100):
    times = []
    for _ in range(repetitions):
        target = random.choice(comics).title  # Pilih target acak
        start_time = time.time()
        binary_search_recursive_with_delay(comics, target, key, 0, len(comics) - 1)
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)


sizes = [10, 50, 100, 500, 1000, 2000, 5000, 10000]
insertion_sort_iterative_times = []
binary_search_recursive_times_with_variation = []

# Prepare table data for tabular output
table_data = []

for size in sizes:
    # Generate random comics
    comics = [Comic(f"Comic {i}", f"Genre {random.randint(1, 10)}") for i in range(size)]
    random.shuffle(comics)

    iterative_sort_comics = comics[:]
    iterative_sort_time = measure_iterative_sort_time(iterative_sort_comics, "title")
    insertion_sort_iterative_times.append(iterative_sort_time)

    iterative_sort_comics.sort(key=lambda comic: comic.title)  # Ensure the list is sorted before searching
    search_time = measure_recursive_search_time_with_variation(iterative_sort_comics, "title", repetitions=5)
    binary_search_recursive_times_with_variation.append(search_time)

    table_data.append([size, iterative_sort_time, search_time])

def main_menu():
    while True:
        print("\n=== Menu ===")
        print("1. Sort Komik")
        print("2. Pencarian Komik")
        print("3. Keluar")
        choice = input("Pilih opsi (1-3): ")

        if choice == '1':
            size = int(input("Masukkan jumlah komik yang ingin dibuat: "))
            comics = [Comic(f"Comic {i}", f"Genre {random.randint(1, 10)}") for i in range(size)]
            random.shuffle(comics)

            # Ukur waktu pengurutan
            sort_time = measure_iterative_sort_time(comics, "title")
            insertion_sort_iterative(comics, "title")
            print(f"\nKomik telah diurutkan berdasarkan judul. Waktu pengurutan: {sort_time:.6f} detik.")
            for comic in comics:
                print(comic)

        elif choice == '2':
            size = int(input("Masukkan jumlah komik yang ingin dibuat: "))
            comics = [Comic(f"Comic {i}", f"Genre {random.randint(1, 10)}") for i in range(size)]
            random.shuffle(comics)

            # Ukur waktu pengurutan
            sort_time = measure_iterative_sort_time(comics, "title")
            insertion_sort_iterative(comics, "title")
            print(f"\nKomik telah diurutkan berdasarkan judul. Waktu pengurutan: {sort_time:.6f} detik.")

            target_title = input("Masukkan judul komik yang ingin dicari: ")
            search_time = measure_recursive_search_time_with_variation(comics, "title", repetitions=5)
            print(f"Waktu pencarian: {search_time:.6f} detik.")

        elif choice == '3':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main_menu()

print("\n=== Tabel Tabular Waktu Pengurutan dan Pencarian ===")
headers = ["Ukuran Data", "Waktu Pengurutan (Iterative)", "Waktu Pencarian (Recursive)"]
print(tabulate(table_data, headers=headers, tablefmt="grid"))

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(sizes, insertion_sort_iterative_times, marker='o', label="Iterative Insertion Sort", color='green')
plt.title("Insertion Sort Time Complexity (Iterative)")
plt.xlabel("Number of Comics")
plt.ylabel("Time (seconds)")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(sizes, binary_search_recursive_times_with_variation, marker='o', label="Recursive Binary Search", color='purple')
plt.title("Binary Search Time Complexity (Recursive with Variation)")
plt.xlabel("Number of Comics")
plt.ylabel("Time (seconds)")
plt.legend()

plt.tight_layout()
plt.show()
