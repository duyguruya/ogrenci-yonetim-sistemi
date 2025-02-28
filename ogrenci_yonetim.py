ogrenciler = {}  # Öğrenci bilgilerini saklamak için sözlük

def ogrenci_ekle():
    ad = input("Öğrencinin adı: ")
    soyad = input("Öğrencinin soyadı: ")
    numara = input("Öğrencinin numarası: ")
    bolum = input("Öğrencinin bölümü: ")
    not_ortalamasi = float(input("Öğrencinin not ortalaması: "))

    ogrenciler[numara] = {
        "ad": ad,
        "soyad": soyad,
        "bolum": bolum,
        "not_ortalamasi": not_ortalamasi
    }
    print(f"{numara} numaralı öğrenci eklendi.")

def ogrenci_goruntule():
    numara = input("Öğrenci numarası (tümü için boş bırakın): ")
    if numara:
        if numara in ogrenciler:
            ogrenci = ogrenciler[numara]
            print(f"Numara: {numara}")
            print(f"Ad: {ogrenci['ad']}")
            print(f"Soyad: {ogrenci['soyad']}")
            print(f"Bölüm: {ogrenci['bolum']}")
            print(f"Not Ortalaması: {ogrenci['not_ortalamasi']}")
        else:
            print(f"{numara} numaralı öğrenci bulunamadı.")
    else:
        for numara, ogrenci in ogrenciler.items():
            print(f"Numara: {numara}")
            print(f"Ad: {ogrenci['ad']}")
            print(f"Soyad: {ogrenci['soyad']}")
            print(f"Bölüm: {ogrenci['bolum']}")
            print(f"Not Ortalaması: {ogrenci['not_ortalamasi']}")
            print("-" * 20)

def ogrenci_guncelle():
    numara = input("Güncellenecek öğrencinin numarası: ")
    if numara in ogrenciler:
        ogrenci = ogrenciler[numara]
        ad = input(f"Yeni ad ({ogrenci['ad']}): ") or ogrenci['ad']
        soyad = input(f"Yeni soyad ({ogrenci['soyad']}): ") or ogrenci['soyad']
        bolum = input(f"Yeni bölüm ({ogrenci['bolum']}): ") or ogrenci['bolum']
        not_ortalamasi = input(f"Yeni not ortalaması ({ogrenci['not_ortalamasi']}): ")
        if not_ortalamasi:
            not_ortalamasi = float(not_ortalamasi)
        else:
            not_ortalamasi = ogrenci['not_ortalamasi']

        ogrenciler[numara] = {
            "ad": ad,
            "soyad": soyad,
            "bolum": bolum,
            "not_ortalamasi": not_ortalamasi
        }
        print(f"{numara} numaralı öğrenci güncellendi.")
    else:
        print(f"{numara} numaralı öğrenci bulunamadı.")

def ogrenci_sil():
    numara = input("Silinecek öğrencinin numarası: ")
    if numara in ogrenciler:
        del ogrenciler[numara]
        print(f"{numara} numaralı öğrenci silindi.")
    else:
        print(f"{numara} numaralı öğrenci bulunamadı.")

while True:
    print("\nÖğrenci Yönetim Sistemi")
    print("1. Öğrenci Ekle")
    print("2. Öğrenci Görüntüle")
    print("3. Öğrenci Güncelle")
    print("4. Öğrenci Sil")
    print("5. Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        ogrenci_ekle()
    elif secim == "2":
        ogrenci_goruntule()
    elif secim == "3":
        ogrenci_guncelle()
    elif secim == "4":
        ogrenci_sil()
    elif secim == "5":
        break
    else:
        print("Geçersiz seçim.")                                