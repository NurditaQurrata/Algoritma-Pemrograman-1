kata = input("Masukkan kata/kalimat yang ingin di cek: ")
panjang = len(kata)
kondisi = True

for i in range(0, panjang):
    if(kondisi):
        a = panjang-(i+1)
        if kata[i] is kata[a]:
            kondisi = True
        else:
            kondisi = False
if(kondisi):
    print("Polindrom")
else:
    print("Bukan Polindrom")
    
