def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))

            if value <= 0:
                print("HATA: Değer 0'dan büyük olmalıdır.")
                continue

            return value

        except ValueError:
            print("HATA: Lütfen geçerli bir tam sayı giriniz.")


def get_non_negative_integer(message):
    while True:
        try:
            value = int(input(message))

            if value < 0:
                print("HATA: Değer negatif olamaz.")
                continue

            return value

        except ValueError:
            print("HATA: Lütfen geçerli bir tam sayı giriniz.")


def get_non_empty_text(message):
    while True:
        value = input(message).strip()

        if not value:
            print("HATA: Bu alan boş bırakılamaz.")
            continue

        return value