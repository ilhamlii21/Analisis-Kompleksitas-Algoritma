# 📚 Comic Sort & Search Performance Visualizer

Project ini adalah simulasi interaktif untuk **mengurutkan** dan **mencari komik** berdasarkan judul menggunakan:
- **Insertion Sort (Iteratif)**
- **Binary Search (Rekursif dengan variasi delay)**

Dengan tampilan menu CLI (Command-Line Interface) dan grafik performa untuk analisis waktu!

---

## 🚀 Fitur Utama

🔢 **Sorting Komik**  
- Menggunakan metode *Iterative Insertion Sort*  
- Mengukur waktu eksekusi untuk berbagai ukuran data  

🔍 **Pencarian Komik**  
- Menggunakan *Recursive Binary Search*  
- Diberi variasi delay untuk mensimulasikan beban komputasi  
- Mengukur rata-rata waktu pencarian  

📊 **Visualisasi Waktu Eksekusi**  
- Grafik waktu pengurutan dan pencarian menggunakan `matplotlib`

📋 **Tabel Hasil**  
- Tabel waktu pengurutan dan pencarian per ukuran data menggunakan `tabulate`

---

## 📦 Struktur Kode

- `Comic`: Class data untuk komik (`title`, `genre`)
- `insertion_sort_iterative`: Pengurutan judul komik secara iteratif
- `binary_search_recursive_with_delay`: Pencarian biner dengan delay simulatif
- `main_menu`: Menu interaktif CLI
- `matplotlib`: Menampilkan grafik hasil
- `tabulate`: Menampilkan hasil dalam bentuk tabel

---

## 🛠️ Cara Menjalankan

1. Pastikan Python sudah terinstal (direkomendasikan versi 3.8+)
2. Install dependensi:
   ```bash
   pip install matplotlib tabulate
