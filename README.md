# PA-DDP-C-Kelompok-7

# PROFIL
### Kelompok 7
Judul program = DASAR DASAR PEMROGRAMAN
SISTEM PEMESANAN TIKET WISATA

### Anggota
Nama = Chaesarrio Taufiqul Hakim 
NIM = 2409116096

Nama = Nanda Pesona Putri 
NIM = 2409116101

Nama = Dimas Aji Mukti
NIM =2409116107

# FLOWCHART
![image](https://github.com/user-attachments/assets/62234ac2-3ab7-43d7-ba41-0b22d6b347e6)

![image](https://github.com/user-attachments/assets/27731d02-e96f-428b-a22e-74572834af30)

![image](https://github.com/user-attachments/assets/50a6539c-175f-4cd3-8694-38f156658668)

Ketiga Gambar diatas merupakan Flowchart dari program yang kami buat

# OUTPUT
## Menu awal

![image](https://github.com/user-attachments/assets/e35ccbd6-d45a-4403-b385-40d5dd017fc9)

Gambar diatas merupakan menu awal dari program kami yang dimana terdapat 3 pilihan dan terdapat out put jika memilih selaindari 3 pilihan di atas

### penjelasan Pilihan
### 1) Jika memilih menu no 1

![image](https://github.com/user-attachments/assets/e4d3b30d-7fad-4459-9eb0-f1443d4293d0)

maka akan menampilkan login admin yang dimana kita disuruh untuk melakukan input username dan password dan akan mengecek role apakah yang dimiliki user jika role = user makan akan menampilkan menu user dan jika role = admin akan menampilkan menu admin

###  2) Jika memilih menu no 2

![image](https://github.com/user-attachments/assets/b50587ec-6945-4d69-a89b-0fca02ebdcb1)

maka akan memanggil fungsi register

###  3) jika memilih menu no 3

![image](https://github.com/user-attachments/assets/8c58d5fe-f191-46b9-844f-bc6d542ba0f3)

maka program akan dihentikan

 ## Penjelasan lebih dalam tentang fungsi registrasi

### 1) input nama dan password
 
 ![image](https://github.com/user-attachments/assets/1faaf561-31cb-45b1-9326-be2992165407)
  
pertama-tama akan kalian akan disuruh untuk melakukan input username dan password

### 2) input saldo

![image](https://github.com/user-attachments/assets/58ceea92-5430-4ff0-9892-0489c5a96969)

selanjutnya memasukan saldo untuk melakukan pembelian nantinya

![image](https://github.com/user-attachments/assets/07b97912-1bfa-4c08-a177-eef00b1d78f0)

jika berhasil maka akan keluar output seperti diatas dan akan langsung diarahkan ke user menu

## Penjelasan lebih dalam tentang menu login
Terdapat dua kondisi saat melakukan login 

### 1)Kondisi pertama
   jika role = admin setelah mengisi username dan password

![image](https://github.com/user-attachments/assets/bb97fc9f-e15b-4ddb-a766-7135e7c52b7f)

maka akan menampilkan menu admin pada menu seperti pada gambar diatas

### 2) Kondisi kedua 
   jika role = user setelah mengisi username dan password

![image](https://github.com/user-attachments/assets/f608b7c9-fdbd-44ab-81a6-5744648afaa6)

   maka akan menampilkan menu user pada menu seperti pada gambar diatas

## Penjelasan Menu user berserta

### 1) Lihat daftar wisata

![image](https://github.com/user-attachments/assets/539d892b-4dac-41d0-becb-25a0a8cde29b)

ketika memilih menu dafatr wisata maka akan menampilkan dafatr wisata yang kami tawarkan menggunakan pretty table

### 2) Pesan tiket

![image](https://github.com/user-attachments/assets/27956d07-c91e-4725-9864-1574e7e620ad)

ketika memilih menu kedua pesan tiket maka pertama tama akan menampilkan daftar wisata terlebih dahulu

![image](https://github.com/user-attachments/assets/b842ae8f-390b-42b1-a909-c965bb600f94)

setelah itu maka akan memasukan tiket apa yang dipesan dengan memasukan ID tiket lalu masukan berapa tiket yang akan dipesan

![image](https://github.com/user-attachments/assets/0773a94b-0f1b-40c7-a621-49d23a14013e)

ketika berhasil maka akan menampilkan struk seperti pada gambar diatas

![image](https://github.com/user-attachments/assets/981bf6ab-e808-4c5f-a770-e3f1cf306638)

output jika ID tidak ditemukan

![image](https://github.com/user-attachments/assets/8d3f67f5-7d72-4cb7-ac9c-f830edcb85d3)

output jika saldo tidak mencukupi

### 3) Top up saldo

![image](https://github.com/user-attachments/assets/cabc45ef-dfff-4332-bcb7-a1807143d134)

pertama tama memasukan berapa jumlah saldo yang ingin dimasukan dan ketika berhasil akan menampilkan output bahwa pengisian saldo berhasil dan akan menampilkan jumlah saldo sekarang

![image](https://github.com/user-attachments/assets/c50f2f34-f01f-4002-8cc0-384ca438f79a)

output jika mengisi saldo lebih dari 5 juta

### 4) Tampilkan saldo

![image](https://github.com/user-attachments/assets/3591aba2-9adf-4369-a939-b3dd75daaf43)

ketika memilih menu menampilkan saldo maka akan keluar out saldo sekarang seperti pada kambar diatas

### 5) Keluar

![image](https://github.com/user-attachments/assets/233c13c5-f6be-44ee-87fd-264328cbc752)

ketika memilih menu keluar maka akan kembali ke menu awal

### 6) Jika memilih diluar dari opsi pilihan

![image](https://github.com/user-attachments/assets/cc238d1c-0900-4610-a993-8f9707e6cc26)

maka akan menampilkan output bahwa pilihan tidak valid

## Penjelasan menu admin

### 1) Tambah wisata

![image](https://github.com/user-attachments/assets/9a16c0ca-a567-4d0d-aec8-72177c6ad1f2)

ketika memilih menu tambah wisata maka pertama tama akan melakukan input wisata yang baru lalu input harganya dan ketika berhasil maka akan ada output penambahan berhasil seperti pada gambar

### 2) Ubah wisata

![image](https://github.com/user-attachments/assets/ab2305fc-7d9f-454b-b3e7-4447df357cb8)

jika memilih menu ubah wisata maka pertama tama akan menampilkan daftar wisata

![image](https://github.com/user-attachments/assets/72314e0c-b81b-4017-a989-bba7f7fdf589)

selanjutnya akan melakukan input ID wisata lalu masukan harga baru ketika pengubahan berhasil maka akan menampilkan bahwa pengubahan berhasil seperti pada gambar

![image](https://github.com/user-attachments/assets/c3c5c031-5397-4085-b2aa-0e92b4df36e4)

output jika ID tidak ditemukan

### 3) Hapus wisata

![image](https://github.com/user-attachments/assets/67bb6f8c-2919-4a5c-8243-a9a82210f4ce)

ketika memilih menu hapus wisata maka pertama tama akan menampilkan daftar wisata kemudian melakukan input ID wisata yang ingin dihapus dan jika berhasil akan menampilkan output seperti pada gambar diatas

![image](https://github.com/user-attachments/assets/dd41de8a-196f-4585-92be-b2e5ddfcdbec)

output jika ID tidak ditemukan

### 4) Lihat daftar wisata

![image](https://github.com/user-attachments/assets/539d892b-4dac-41d0-becb-25a0a8cde29b)

ketika memilih menu dafatr wisata maka akan menampilkan dafatr wisata yang kami tawarkan menggunakan pretty table

### 5) Keluar

![image](https://github.com/user-attachments/assets/233c13c5-f6be-44ee-87fd-264328cbc752)

ketika memilih menu keluar maka akan kembali ke menu awal

### 6) Jika memilih diluar dari opsi pilihan

![image](https://github.com/user-attachments/assets/cc238d1c-0900-4610-a993-8f9707e6cc26)

maka akan menampilkan output bahwa pilihan tidak valid
