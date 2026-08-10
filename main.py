from widget_provider import get_widget
from text_loader import load_texts

from font_parser import parse_font_file

from text_overflow import (
    check_text_overflow,
    check_text_height_overflow
)


def main():

    print("===== TFT Overflow Analyzer =====\n")

    # Widget bilgilerini al
    widget = get_widget()

    # Seçilen font dosyasını parse et
    font_widths, font_height = parse_font_file(
        widget.font_path
    )

    print("\nFont bilgileri okundu.")
    print(f"Seçilen Font : {widget.font}")
    print(f"Font Height  : {font_height} px")

    # Textleri oku
    texts = load_texts("texts.txt")

    print("\nAnaliz Başlıyor...\n")

    pass_count = 0
    fail_count = 0

    # TFT'nin başlangıç yüksekliği
    remaining_height = widget.height

    for text in texts:

        # ----------------------------------------
        # YATAY KONTROL
        # ----------------------------------------

        horizontal_overflow = check_text_overflow(
            text,
            widget.width,
            font_widths
        )

        # ----------------------------------------
        # DİKEY KONTROL
        # ----------------------------------------

        vertical_overflow = check_text_height_overflow(
            remaining_height,
            font_height
        )

        print("-" * 50)

        print(f"Text : {text}")

        # ----------------------------------------
        # YATAY SONUÇ
        # ----------------------------------------

        if horizontal_overflow > 0:

            print("Yatay Durum : FAIL")
            print(
                f"Yatay Overflow : "
                f"{horizontal_overflow} px"
            )

            horizontal_fail = True

        else:

            print("Yatay Durum : PASS")

            if horizontal_overflow == 0:

                print("Yatay olarak tam sığıyor.")

            else:

                print(
                    f"Yatay boşluk : "
                    f"{-horizontal_overflow} px"
                )

            horizontal_fail = False

        # ----------------------------------------
        # DİKEY SONUÇ
        # ----------------------------------------

        if vertical_overflow > 0:

            print("Dikey Durum : FAIL")

            print(
                f"Dikey Overflow : "
                f"{vertical_overflow} px"
            )

            vertical_fail = True

        else:

            print("Dikey Durum : PASS")

            remaining_height -= font_height

            print(
                f"Kalan yükseklik : "
                f"{remaining_height} px"
            )

            vertical_fail = False

        # ----------------------------------------
        # GENEL SONUÇ
        # ----------------------------------------

        if not horizontal_fail and not vertical_fail:

            pass_count += 1

        else:

            fail_count += 1

    # ----------------------------------------
    # ÖZET
    # ----------------------------------------

    print("\n==============================")

    print("ÖZET")

    print(f"Toplam : {len(texts)}")
    print(f"PASS : {pass_count}")
    print(f"FAIL : {fail_count}")

    print(
        f"Kalan TFT yüksekliği : "
        f"{remaining_height} px"
    )


if __name__ == "__main__":
    main()