### PRAKTIKUM 5
### USWATUN HASANAH
### 312210343
### TI.22.A3

### MEMBUAT LIST SEBANYAK 5 ELEMEN
### AKSES LIST

Tampilkan elemen ke-3 lalu ambil nilai elemen ke-2 sampai elemen ke-4 dan elemen terakhir

`
print('#Akses List')
r = [8,6,4,9,2]
print(r)
print('- Elemen ke-3 : ', r[3])
print('-Nilai Elemen ke-2 sampai elemen ke-4 : ',r[2:5])
print('-Elemen terakhir : ', r[-1])
`

(https://user-images.githubusercontent.com/115516474/202911294-7046d079-ad6a-4f87-a06d-bd108170c169.png)



### MENGUBAH ELEMEN LIST

`
print('# Mengubah Elemen List')
a = ['rose','jiso',6,18,21]
print(a)
a[1]='jenie kim'
print('- mengubah data kedua : ', a)
a[4:5]=12,16
print('- mengubah data ke-4 sampai terakhir: ', a)
print(a)
`

Mengubah elemen ke-4 dengan nilai yang lain sampai dengan elemen terakhir

![1](https://user-images.githubusercontent.com/115516474/202912041-4a5756e4-db5b-44db-bcce-f0c8027824a3.png)



### MENAMBAH ELEMEN LIST

`
print('# Menambahkan Elemen List')
n = ['sendok', 'garpu', 'piring', 'gelas', 'sumpit']
print(n)
A = n[0:2]
B = n[2:]
print(A)
print(B)
B.append('garpu')
print('- Menambahkan list B Dengan Nlai String : ', B)
B.extend([4,2,1])
print('- Menambahkan List B Dengan 3 Nilai : ',B)
B.extend(A)
print('-Menggabungkan List B Dengan List A : ', B)
`

Mengambil 2 bagian dari list pertama lalu jadikan list ke-2. Tambhakan list ke-2 dengan 3 nilai, lalu gabungkan ke-dua list 

![3](https://user-images.githubusercontent.com/115516474/202911350-9805facc-ba63-4e5b-bb8d-e7cc51e0d1f9.png)



### TUGAS 
### BUAT PROGRAM SEDERHANA 

Membuat progam sederhana untuk menambahkan data kedalam sebuah List dengan mengunakan perulangan. lalu tampilkan pertanyaan unuk menambahkan data contoh 
(y/t). Apabila menjawab "t"(tidak) maka data otomatis akan ditampilan dan masukan nilai akhir, nilai diambil dari perhitungan 3 konseponen nilai 
(Tugas 30%, Uts 35%, Uas 35%)



`
data = []
stop = False

while(not stop):
    nama = input("Nama : ")
    nim = input("NIM : ")
    tugas = int(input("Nilai Tugas : "))
    uts = int(input("Nilai UTS : "))
    uas = int(input("Nilai UAS : "))
    akhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)
    data.append([nama,nim,tugas,uts,uas,int(akhir)])

    tanya = input('Tambahkan Data (y/t) ? ')
    if (tanya == 't'):
        stop = True

print("==================================================================")
print("| No |    Nama      |  NIM  | Tugas |  UTS  |  UAS  |  Akhir |")
print("==================================================================")

i = 0

for nilai in data:
    i += 1
print("| {no}  | {nama:12s} | {nim:5s} | {tugas:5d} | {uts:5d} | {uas:5d} |{akhir:6.2f} |
".format(no=i, nama=nilai[0], nim=nilai[1], tugas=nilai[2],uts=nilai[3],uas=nilai[4],akhir=nilai[5]))

print("==================================================================")
`


![4](https://user-images.githubusercontent.com/115516474/202911377-ff6b4174-f26d-41aa-825e-6b4819360d64.png)


### FLOWCHART

![5](https://user-images.githubusercontent.com/115516474/202911396-e944194b-444f-4195-9c0f-ecf6f565e8eb.png)


