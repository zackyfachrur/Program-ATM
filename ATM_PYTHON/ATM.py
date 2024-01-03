def informasi():
    print("==========================")
    print(" SELAMAT DATANG DI ATM ABC ")
    print("MASUKKAN INFORMASI BERUPA:")
    print("==========================")
    print("NPM           ")
    print("==========================")
    print("NAMA          ")
    print("==========================")
    print("NO. REKENING   ")
    print("==========================")

    informasi_1 = input("Ketikkan NPM anda : ")
    print("==========================")
    informasi_2 = input("Ketikkan NAMA anda : ")
    print("==========================")
    informasi_3 = input("Ketikkan NO. REKENING anda : ")
    print("==========================")
    informasi_pin = input("Masukkan PIN anda (6 digit pertama NPM) : ")
    
    informasi_digit = int(informasi_1[:6])

    if informasi_pin == str(informasi_digit):
        print("PIN ANDA BENAR")
        saldo = 1000000

        print("==========================")
        print("1. Cek Saldo           ")
        print("==========================")
        print("2. Tarik Uang          ")
        print("==========================")
        print("3. Setor Uang          ")
        print("==========================")

        menu_informasi = int(input("Masukkan pilihan anda : "))

        if menu_informasi == 1:
            informasi_cek(informasi_1, informasi_2, informasi_3, saldo)
        elif menu_informasi == 2:
            menu_tarik = int(input("Masukkan nominal yang akan ditarik : "))
            tarik = saldo - menu_tarik
            informasi_cek(informasi_1, informasi_2, informasi_3, tarik)
        elif menu_informasi == 3:
            menu_setor = int(input("Masukkan nominal yang akan ditambah : "))
            tambah = saldo + menu_setor
            informasi_cek(informasi_1, informasi_2, informasi_3, tambah)
        else:
            print("Maaf pilihan anda salah")
            print("==========================")

def informasi_cek(npm, nama, no_rekening, saldo):
    print("NPM ANDA : ", npm)
    print("NAMA ANDA : ", nama)
    print("NO. REKENING ANDA : ", no_rekening)
    print("SALDO ANDA : ", saldo)
    print("==========================")

informasi()

