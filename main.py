from widget_provider import get_widget
from text_loader import load_texts
from text_overflow import (
    check_text_overflow,
    check_text_height_overflow
)


def main():

    print("===== TFT Overflow Analyzer =====\n")

    widget = get_widget()

    texts = load_texts("texts.txt")

    print("\nAnaliz Başlıyor...\n")

    pass_count = 0
    fail_count = 0

    for text in texts:

        horizontal_overflow = check_text_overflow(
            text,
            widget.width
        )

        vertical_overflow = check_text_height_overflow(
            widget.height
        )

        print("-" * 50)

        print(f"Text : {text}")

        # Yatay kontrol
        if horizontal_overflow > 0:

            print("Yatay Durum : FAIL")
            print(f"Yatay Overflow : {horizontal_overflow} px")

            fail_count += 1

        else:

            print("Yatay Durum : PASS")

            if horizontal_overflow == 0:
                print("Yatay olarak tam sığıyor.")
            else:
                print(
                    f"Yatay boşluk : {-horizontal_overflow} px"
                )

        # Dikey kontrol
        if vertical_overflow > 0:

            print("Dikey Durum : FAIL")
            print(f"Dikey Overflow : {vertical_overflow} px")

            if horizontal_overflow <= 0:
                fail_count += 1

        else:

            print("Dikey Durum : PASS")

            if vertical_overflow == 0:
                print("Dikey olarak tam sığıyor.")
            else:
                print(
                    f"Dikey boşluk : {-vertical_overflow} px"
                )

        # Genel sonuç
        if horizontal_overflow <= 0 and vertical_overflow <= 0:
            pass_count += 1

    print("\n==============================")

    print("ÖZET")

    print(f"Toplam : {len(texts)}")
    print(f"PASS : {pass_count}")
    print(f"FAIL : {fail_count}")


if __name__ == "__main__":
    main()