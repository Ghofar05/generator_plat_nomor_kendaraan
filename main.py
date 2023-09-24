import random

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
    rand_one = 0 #randomize
    rand_two = 0
    angka_satu = 0
    angka_puluh = 0
    angka_ratus = 0
    angka_ribu = 0
    for i in range(0,jumlah):
        doc.write(hurufdpn +" "+ str(angka_ribu + angka_ratus + angka_puluh + angka_satu) +" "+ str(hubel[rand_one])+str(hubel[rand_two])+"\n") # membuka dan menulis dokumen yang sudah dibuat tadi
        print(hurufdpn +" "+ str(angka_ribu + angka_ratus + angka_puluh + angka_satu) +" "+ str(hubel[rand_one])+str(hubel[rand_two]))
        angka_satu += 1
        if angka_satu == 10:
            angka_puluh +=1
        elif angka_puluh == 10:
            angka_ratus +=1
        elif angka_ratus == 10:
            angka_ribu +=1

        rand_one = random.randint(0,25)
        rand_two = random.randint(0,25)


    doc.close() #menutup dokumen setelah kita buka


main("N",100,"malang")
main("B",100,"jakarta")

