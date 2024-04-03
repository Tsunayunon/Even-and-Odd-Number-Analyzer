def main():
    try:
        sayi_adedi = int(input("Kaç sayı gireceksiniz? "))
        sayilar = []

        for i in range(sayi_adedi):
            sayi = float(input(f"{i+1}. sayıyı girin: "))
            sayilar.append(sayi)

        tek_sayilar = [sayi for sayi in sayilar if sayi % 2 == 1]
        cift_sayilar = [sayi for sayi in sayilar if sayi % 2 == 0]

        tek_sayi_toplam = sum(tek_sayilar)
        tek_sayi_ortalama = tek_sayi_toplam / len(tek_sayilar) if len(tek_sayilar) > 0 else 0

        cift_sayi_toplam = sum(cift_sayilar)
        cift_sayi_ortalama = cift_sayi_toplam / len(cift_sayilar) if len(cift_sayilar) > 0 else 0

        print("\nTek Sayılar:")
        print(f"Toplam: {tek_sayi_toplam}")
        print(f"Ortalama: {tek_sayi_ortalama}")

        print("\nÇift Sayılar:")
        print(f"Toplam: {cift_sayi_toplam}")
        print(f"Ortalama: {cift_sayi_ortalama}")

    except ValueError:
        print("Geçersiz bir giriş yaptınız. Lütfen sayıları doğru bir şekilde girin.")

if __name__ == "__main__":
    main()
