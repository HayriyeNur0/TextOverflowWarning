from text_overflow import check_text_overflow


def main():

    # Test verileri
    text = "motor kontrol "
    area_width = 70 

    pixel_difference = check_text_overflow(
        text,
        area_width
    )

    if pixel_difference > 0:
        print(f"UYARI: Metin {pixel_difference} piksel taşıyor.")

    elif pixel_difference == 0:
        print("Metin alana tam sığıyor.")

    else:
        print(f"Metin alana sığıyor. {-pixel_difference} piksel boşluk kaldı.")


if __name__ == "__main__":
    main()
