import random
#Bilgisayarın rastgele sayı üretmesini sağlayacak kodu yazabilmek için random modülünü import ediyorum.
def oyunkolay():
    print("Kolay Oyun Modumuza Hoş Geldiniz.\nBu modda 0 ile 20 arasında makinenin tuttuğu sayıyı bilmen gerekecek.")
    #0 ile 21 arasından bir sayı seçmesini istediğim için range komuyunu kullanıyorum ve range 1 değişkenine atıyorum.
    range1 = range(0,21)
    #random.choice komutuyla range 1 değişkenininden bir sayı alıyorum ve i değişkenine atıyorum.
    i = random.choice(range1)
    #5 hak belirliyorum
    hak = 5
    while True:
        tahmin = int(input("Tahmininizi Giriniz :"))
        if tahmin > 20:
            print("0 ile 20 arasında bir sayı giriniz .")
        if tahmin == i:
            print("Tebrikler Bildin Ama Bir Daha ki Sefer Ben Kazanacağım")
            print(i,tahmin)
            break
        else:
            if tahmin < i:
            # her bilemediği zaman haktan 1 eksiltiyorum ve yeni hak değişkenine atıyorum.
                hak -= 1
                hak = hak
                print("Az Söyledin :)\n\nBir hakkın gitti.\n\nKALAN HAK :{}\n\n".format(hak))
                if hak == 0:
                    print("Ben Kazandım HAHAHAHA Tuttuğum Sayıyı Bilemedin.\n ")
                    break
            elif tahmin > i:
                hak -= 1
                hak = hak
                print("Çok Söyledin :)\n\nBir hakkın gitti.\n\nKALAN HAK :{}\n\n".format(hak))
                if hak == 0:
                    print("Ben Kazandım HAHAHAHA Tuttuğum Sayıyı Bilemedin.")
                    break
def oyunorta():
    print("Orta Oyun Modumuza Hoş Geldiniz.\nBu modda 0 ile 50 arasında makinenin tuttuğu sayıyı bilmen gerekecek.")
    range1 = range(0,51)
    i = random.choice(range1)
    hak = 15
    while True:
        tahmin = int(input("Tahmininizi Giriniz :"))
        if tahmin > 50:
            print("0 ile 50 arasında bir sayı giriniz .")
        if tahmin == i:
            print("Tebrikle Bildin Ama Bir Daha ki Sefer Ben Kazanacağım.")
            print(i,tahmin)
            break
        else:
            if tahmin < i:
                hak -= 1
                hak = hak
                print("Az Söyledin :)\n\nBir hakkın gitti.\n\nKALAN HAK :{}\n\n".format(hak))
                if hak == 0:
                    print("Ben Kazandım HAHAHAHA Tuttuğum Sayıyı Bilemedin.")
                    break
            elif tahmin > i:
                hak -= 1
                hak = hak
                print("Çok Söyledin :)\n\nBir hakkın gitti.\n\nKALAN HAK :{}\n\n".format(hak))
                if hak == 0:
                    print("Ben Kazandım HAHAHAHA Tuttuğum Sayıyı Bilemedin.\n")
                    break
def oyunzor():
    print("Zor Oyun Modumuza Hoş Geldiniz.\nBu modda 0 ile 100 arasında makinenin tuttuğu sayıyı bilmen gerekecek.")
    range1 = range(0,101)
    i = random.choice(range1)
    hak == 25
    while True:
        tahmin = int(input("Tahmininizi Giriniz :"))
        if tahmin > 100:
            print("0 ile 100 arasında bir sayı giriniz .")
        if tahmin == i:
            print("Tebrikler Bildin Ama Bir Daha ki Sefere Ben Kazanacağım.")
            print(i,tahmin)
            break
        else:
            if tahmin < i:
                hak -= 1
                hak = hak
                print("Az Söyledin :)\n\nBir hakkın gitti\n\nKALAN HAK :{}".format(hak))
                if hak == 0:
                    print("Ben Kazandım HAHAHAHA Tuttuğğum Sayıyı Bilemedin\n")
                    break
            elif tahmin > i:
                hak -= 1
                hak = hak
                print("Çok Söyledin :)\n\nBir hakkın gitti\n\nKALAN HAK :{}".format(hak))
                if hak == 0:
                    print("Ben Kazandım HAHAHAHA Tuttuğum Sayıyı Bilemedin")
