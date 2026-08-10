import re


def parse_font_file(font_file):
    """
    emWin Font Converter tarafından oluşturulan .c font dosyasını okur.

    Döndürür:
        font_widths -> karakter : yatay ilerleme genişliği
        font_height -> font yüksekliği
    """

    font_widths = {}
    font_height = None

    # --------------------------------------------------
    # DOSYAYI OKU
    # --------------------------------------------------

    with open(
        font_file,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as file:

        content = file.read()

    # --------------------------------------------------
    # FONT HEIGHT
    # --------------------------------------------------

    # Örnek:
    # * Height:      20
    # * Initial font height: 20

    height_match = re.search(
        r"Height:\s*(\d+)",
        content,
        re.IGNORECASE
    )

    if height_match:

        font_height = int(
            height_match.group(1)
        )

    # Eğer üstteki bilgi bulunamazsa,
    # GUI_FONT tanımındaki height değerini kullan.
    if font_height is None:

        height_match = re.search(
            r"GUI_FONT[^=]*=\s*\{.*?"
            r",\s*(\d+)\s*/\*\s*height of font",
            content,
            re.IGNORECASE | re.DOTALL
        )

        if height_match:

            font_height = int(
                height_match.group(1)
            )

    # --------------------------------------------------
    # GUI_CHARINFO TABLOSUNU BUL
    # --------------------------------------------------

    charinfo_start = re.search(
        r"GUI_CHARINFO\s+\w+\[\d+\]\s*=\s*\{",
        content
    )

    if not charinfo_start:

        raise ValueError(
            f"GUI_CHARINFO tablosu bulunamadı: {font_file}"
        )

    # GUI_CHARINFO tablosunun başlangıcından sonrasını al.
    charinfo_content = content[
        charinfo_start.end():
    ]

    # --------------------------------------------------
    # KARAKTERLERİ OKU
    # --------------------------------------------------

    # Örnek gerçek yapı:
    #
    # {   5,   5,  2, acGUI_... } /* code 0020 */
    #
    # {  10,  10,  3, acGUI_... } /* code 0023 */

    pattern = re.compile(
        r"\{\s*"
        r"(\d+)\s*,\s*"      # XSize
        r"(\d+)\s*,\s*"      # XDist
        r"(-?\d+)\s*,\s*"    # XOff
        r"[^}]*?"
        r"\}\s*/\*\s*code\s+"
        r"([0-9A-Fa-f]+)",
        re.IGNORECASE
    )

    matches = pattern.findall(
        charinfo_content
    )

    for match in matches:

        x_size = int(match[0])
        x_dist = int(match[1])
        unicode_value = match[3]

        try:

            character = chr(
                int(unicode_value, 16)
            )

            # Metnin TFT üzerinde yatay olarak
            # ne kadar ilerleyeceğini XDist belirler.
            font_widths[character] = x_dist

        except ValueError:

            continue

    # --------------------------------------------------
    # KONTROL
    # --------------------------------------------------

    if font_height is None:

        raise ValueError(
            f"Font yüksekliği bulunamadı: {font_file}"
        )

    if not font_widths:

        raise ValueError(
            f"Karakter genişlikleri bulunamadı: {font_file}"
        )

    return font_widths, font_height

"""if __name__ == "__main__":

    widths, height = parse_font_file(
        "Fonts/LiberationSans20.c"
    )

    print("Font Height:", height)

    for character in [" ", "M", "i", "W", "o", "t"]:

        print(
            repr(character),
            "->",
            widths.get(character, "Bulunamadı"),
            "px"
        )"""