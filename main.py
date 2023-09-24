
def alfabet(): #generate huruf alfabet a sampai z
    huruf = []
    for i in range(ord("a"), ord("z")+1):
        huruf.append(chr(i).upper())

    return  huruf #array

def angka(jumlah): #generate angka menjadi array, fungsi ini tidak kita pakai
    angka = []
    for i in range(0,jumlah):
        angka.append(i)

    return angka

def main(hurufdpn,jumlah,kota): #fungsi utama, hurufdpn = huruf depan, jumlah = jumblah yang ingin digenerate, kota = nama file
    doc = open(f"{kota}.txt","w") #membuat dokumen untuk output
    huruf_depan = hurufdpn
    hubel = alfabet()
    indexhubel = 0 #indexing alfabet
    angka_satu = 0
    angka_puluh = 0
    angka_ratus = 0
    angka_ribu = 0
    for i in range(0,jumlah):
        doc.write(hurufdpn +" "+ str(angka_ribu + angka_ratus + angka_puluh + angka_satu) +" "+ str(hubel[indexhubel])+"\n") # membuka dan menulis dokumen yang sudah dibuat tadi
        print(hurufdpn +" "+ str(angka_ribu + angka_ratus + angka_puluh + angka_satu) +" "+ str(hubel[indexhubel]))
        angka_satu += 1
        if angka_satu == 10:
            angka_puluh +=1
        elif angka_puluh == 10:
            angka_ratus +=1
        elif angka_ratus == 10:
            angka_ribu +=1

        indexhubel += 1
        if indexhubel == 25:
            indexhubel = 0


    doc.close() #menutup dokumen setelah kita buka


main("N",100,"malang")
main("B",100,"jakarta")

