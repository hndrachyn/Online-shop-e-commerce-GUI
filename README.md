# Online Shop E-Commerce GUI

Aplikasi desktop toko online berbasis GUI Python (Tkinter), dikerjakan sebagai proyek kelompok. Desain antarmuka dibuat di Figma, lalu diimplementasikan dengan Python.

## Fitur

- Pendaftaran dan login pengguna dengan username dan password (data disimpan di berkas CSV).
- Tampilan produk, keranjang, checkout, dan pembayaran dalam antarmuka grafis.
- Pencatatan data pembayaran ke berkas CSV.
- Integrasi bot Telegram (kelas `TelegramBot`) dengan `python-telegram-bot`.

## Isi repositori

| Berkas | Keterangan |
|---|---|
| `Online Shop.py` | Kode utama aplikasi |
| `UI UX Gui ecommerce` | Tautan ke desain UI/UX di Figma |
| `Image 1.zip`, `Image 2.zip`, `Image 3.zip` | Aset gambar antarmuka |
| `.github/workflows/python-package.yml` | Alur GitHub Actions untuk pengecekan pada Python 3.9 sampai 3.11 |

## Teknologi

Python, Tkinter, Pillow, pandas, PySimpleGUI, requests, python-dotenv, python-telegram-bot.

## Cara menjalankan

1. Pasang Python 3.9 atau lebih baru.
2. Pasang pustaka yang dipakai: `pillow`, `pandas`, `PySimpleGUI`, `requests`, `python-dotenv`, `python-telegram-bot` (versi yang memakai `Updater`).
3. Ekstrak aset gambar dari berkas zip.
4. Untuk fitur bot Telegram, siapkan token bot Anda sendiri dari BotFather (token tidak disertakan di repositori).
5. Jalankan: `python "Online Shop.py"`.

## Catatan

Kode utama masih berada dalam satu berkas besar. Memecahnya menjadi beberapa modul akan memudahkan pemeliharaan.
