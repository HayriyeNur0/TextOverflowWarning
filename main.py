from widget_provider import get_widget
from text_loader import load_texts
from text_overflow import check_text_overflow


def main():

    print("===== TFT Overflow Analyzer =====\n")

    widget = get_widget()

    texts = load_texts("texts.txt")

    print("\nAnaliz Başlıyor...\n")

    pass_count = 0
    fail_count = 0

    for text in texts:

        pixel_difference = check_text_overflow(
            text,
            widget.width
        )

        print("-" * 50)

        print(f"Text : {text}")

        if pixel_difference > 0:

            print("Durum : FAIL")

            print(f"Overflow : {pixel_difference} px")

            fail_count += 1

        elif pixel_difference == 0:

            print("Durum : PASS")

            print("Tam sığıyor.")

            pass_count += 1

        else:

            print("Durum : PASS")

            print(f"Boşluk : {-pixel_difference} px")

            pass_count += 1

    print("\n==============================")

    print("ÖZET")

    print(f"Toplam : {len(texts)}")

    print(f"PASS : {pass_count}")

    print(f"FAIL : {fail_count}")


if __name__ == "__main__":
    main()