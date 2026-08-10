import os


FONT_FOLDER = "Fonts"


def get_fonts():
    """
    Fonts klasöründeki .c font dosyalarını bulur.
    """

    fonts = []

    for file_name in os.listdir(FONT_FOLDER):

        if file_name.lower().endswith(".c"):
            fonts.append(file_name)

    fonts.sort()

    return fonts


def select_font():
    """
    Kullanıcıya mevcut fontları numaralı olarak gösterir
    ve seçilen fontun dosya yolunu döndürür.
    """

    fonts = get_fonts()

    if not fonts:
        print("Fonts klasöründe .c font dosyası bulunamadı.")
        return None, None

    print("\n===== FONT SEÇİMİ =====\n")

    for i, font_file in enumerate(fonts, start=1):

        font_name = os.path.splitext(font_file)[0]

        print(f"{i} - {font_name}")

    print()

    while True:

        try:
            choice = int(input("Font numarasını seçiniz: "))

            if 1 <= choice <= len(fonts):

                selected_file = fonts[choice - 1]

                font_name = os.path.splitext(
                    selected_file
                )[0]

                font_path = os.path.join(
                    FONT_FOLDER,
                    selected_file
                )

                print(f"\nSeçilen font: {font_name}")

                return font_path, font_name

            print("Geçersiz seçim. Listeden bir numara seçiniz.")

        except ValueError:

            print("Lütfen sadece numara giriniz.")

if __name__ == "__main__":
    select_font()
