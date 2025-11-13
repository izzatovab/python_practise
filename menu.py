def buyurtma_olish():
    menyu = [
        {"name": "Osh", "price": 25000},
        {"name": "Shashlik", "price": 18000},
        {"name": "Lag'mon", "price": 20000},
        {"name": "Salat 'Achchiq-chuchuk'", "price": 8000},
        {"name": "Choy", "price": 5000},
        {"name": "Sharbat", "price": 10000},
        {"name": "Kofe", "price": 12000},
        {"name": "Non", "price": 3000}
    ]

    tanlanganlar = []

    while True:
        print("\n🍴 Restoran Menyusi:")
        for i, item in enumerate(menyu, 1):
            print(f"{i}. {item['name']} — {item['price']} so‘m")

        try:
            tanlov = int(input("\nQaysi ovqatni olasiz? (raqam kiriting): "))
            if 1 <= tanlov <= len(menyu):
                miqdor = int(input(f"{menyu[tanlov - 1]['name']} nechta olasiz? "))
                tanlanganlar.append({
                    "name": menyu[tanlov - 1]["name"],
                    "price": menyu[tanlov - 1]["price"],
                    "quantity": miqdor
                })
            else:
                print("❌ Noto‘g‘ri raqam kiritildi.")
                continue
        except ValueError:
            print("❌ Iltimos, raqam kiriting.")
            continue

        davom = input("\nSiz yana buyurtma qilasizmi? (ha/yo‘q): ").strip().lower()
        if davom in ["yoq", "yo‘q", "no"]:
            break
        elif davom not in ["ha", "xa", "yes"]:
            print("❗ Noma’lum javob. Buyurtma yakunlanadi.")
            break

    return tanlanganlar
