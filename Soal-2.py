# Buatlah sebuah program yang dapat menghitung luas lingkaran.
# Program meminta input dari user berupa angka sebagai jari-jari lingkaran.
# Program menghitung luas lingkaran dengan rumus πr² 2
# Π = 22/7
# r = jari - jari lingkaran 
# Lalu tampilkan ke layar dengan format:
# Hint: untuk menampilkan tanda kuadrat gunakan print(“\u00b2”)

r = float(input('Tulis Jari-Jari Lingkaran: '))

# Hitung Luas Lingkaran
luas = (22 / 7) * r ** 2
 
#Menampilkan Hasil Perhitungan
print('Luas lingkaran dengan jari-jari %0.2f cm adalah %0.2f cm'%(r, luas))
