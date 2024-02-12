# TUGAS KECIL 1 IF2211 STRATEGI ALGORITMA

## Deskripsi SIngkat Program

Cyberpunk 2077 Breach Protocol adalah minigame meretas pada permainan video Cyberpunk 2077. Minigame ini merupakan simulasi peretasan jaringan local dari ICE (Intrusion Countermeasures Electronics) pada permainan Cyberpunk 2077. Program ini mengimplementasikan algoritma Brute Force untuk mencari buffer dengan reward tertinggi.

## Komponen pada permainan:

1. Token – terdiri dari dua karakter alfanumerik seperti E9, BD, dan 55.
2. Matriks – terdiri atas token-token yang akan dipilih untuk menyusun urutan kode.
3. Sekuens – sebuah rangkaian token (dua atau lebih) yang harus dicocokkan.
4. Buffer – jumlah maksimal token yang dapat disusun secara sekuensial.
   
## Aturan permainan Breach Protocol:

1. Pemain bergerak dengan pola horizontal, vertikal, horizontal, vertikal (bergantian) hingga
semua sekuens berhasil dicocokkan atau buffer penuh.
2. Pemain memulai dengan memilih satu token pada posisi baris paling atas dari matriks.
3. Sekuens dicocokkan pada token-token yang berada di buffer.
4. Satu token pada buffer dapat digunakan pada lebih dari satu sekuens.
5. Setiap sekuens memiliki bobot hadiah atau reward yang variatif.
6. Sekuens memiliki panjang minimal berupa dua token.
Program berikut merupakan implementasi dari pendekatan Brute Force untuk menyelesaikan mini game dari video game Cyber Punk 2077 (Cyber Punk Breach Protocol)

## Requirement Program

- Python 3.12.0

## Cara Menjalankan Program:

1. Clone repository ini lalu buka folder dan pastikan Anda berada di root directory project ini

```bash
git clone https://github.com/shafiqIrv/Tucil1_13522003.git
```

2. Kunjungi `/bin` dimana file executeable `main.exe` disimpan

```bash
cd main
```

3. Jalankan program utama `main.exe`

```bash
./main
```

## Identitas Pembuat

|   NIM    |        Nama         |
| :------: | :-----------------: |
| 13522003 | Shafiq irvansyah |
