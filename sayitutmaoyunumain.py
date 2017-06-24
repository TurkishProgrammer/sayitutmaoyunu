import oyunfonk
#import oyunfonk diyerek oyunfonk GitHuba eklediğim adıyla sayitutmafonk dosyadındaki fonksiyonları kullanıyorum.
print("Sayı Tahmin Oyunumuza Hoş Geldiniz :)")
# while True döngüsü kurarak kullanıcı istemeden programın sonlanmasını engelliyorum.
while True:
    zorluk = input("İstediğiniz Zorluk Düzeyini Seçiniz :\n(1)Kolay\n(2)Orta\n(3)Zor\n(4)Çıkış")
    if zorluk == "1":
        oyunfonk.oyunkolay()
    elif zorluk == "2":
        oyunfonk.oyunorta()
    elif zorluk == "3":
        oyunfonk.oyunzor()
    elif zorluk == "4":
        break
