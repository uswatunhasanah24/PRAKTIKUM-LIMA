print('#Akses List')
r = [8,6,4,9,2]
print(r)
print('- Elemen ke-3 : ', r[3])
print('-Nilai Elemen ke-2 sampai elemen ke-4 : ',r[2:5])
print('-Elemen terakhir : ', r[-1])

print('# Mengubah Elemen List')
a = ['rose','jiso',6,18,21]
print(a)
a[1]='jenie kim'
print('- mengubah data kedua : ', a)
a[4:5]=12,16
print('- mengubah data kedua : ', a)
print(a)

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