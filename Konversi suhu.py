print("KONVERSI SUHU")
print("1. Fahrenheit to Celcius")
print("2. Kelvin to Celcius")
print("3. Exit")
pilih = int(input("Pilih Menu: "))
while pilih !=3:
    if pilih == 1:
        suhuF=int(input("Masukkan angka: "))
        a=(5/9)*(suhuF-32)
        print(suhuF,"Fahrenheit"," = ",a,"Celcius")
    elif pilih == 2:
        suhuK=int(input("Masukkan angka: "))
        a=suhuK-273
        print(suhuK,"Kelvin"," = ",a,"Celcius")
    else:
        print("Menu Tidak Ada")
    pilih = int(input("Silahkan pilih menu kembali, Jika tidak silahkan tekan tombol '3': "))
print("Terimakasih")



