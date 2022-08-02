# Buatlah sebuah program untuk menentukan apakah seorang siswa lulus ujian atau tidak. 
# Siswa dinyatakan lulus apabila nilai ujian teori dan ujian praktek minimal 70. 
# Program menerima input berupa nilai ujian teori dan praktek, nilai ujian dapat berupa bilangan desimal.

teori = int(input("Masukkan nilai ujian teori: "))
praktek = int(input("Masukkan nilai ujian praktek: "))

if(teori >= 70 and praktek >= 70):
   print('Selamat, anda lulus!')

elif (teori >=70 and praktek <70):
   print('Anda harus mengulang ujian praktek.')

elif (teori <70 and praktek >=70):
   print('Anda harus mengulang ujian teori.')
    
else:
    print('Anda harus mengulang ujian teori dan praktek.')